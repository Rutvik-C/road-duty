import uuid
import cv2
import os
import time
import re
import shutil

from src.utils.ocr import doOCR
from src.classes.detected_object import DetectedObject


def validateLicenseNumber(number):
    if number is None:
        return False
    
    pattern = re.compile("[A-Z]{2}[0-9]{2}[A-Z]{0,3}[0-9]{4}")
    if re.search(pattern, number.upper()) is None:
        return False

    return True


def detectLicense(ip, op, predictor, options):
    while True:
        if ip.empty():
            time.sleep(1)
            continue

        print(f"INFO: DetectLicenseProcess: Detecting license plate in image.")
        packet = ip.get()
        track = packet.track
        
        folder = f"tmp/license_plate/{track.id}"
        os.mkdir(folder)

        predictions = []
        for i, do in enumerate(track.journey):
            img = do.getCroppedImage()
            objData = predictor.getObjectsInImage(img)
            if len(objData) == 0:
                continue

            objData.sort(key=lambda record: record["score"])
            
            imgLoc = f"{folder}/{i}.jpg"
            cv2.imwrite(imgLoc, img)
            doLicensePlate = DetectedObject(imgLoc, objData[-1]["x1"], objData[-1]["x2"], objData[-1]["y1"], objData[-1]["y2"])

            tmpLicenseImgPath = f"{folder}/cropped_{i}.jpg"
            cv2.imwrite(tmpLicenseImgPath, doLicensePlate.getCroppedImage())

            licenseNumber, score = doOCR(tmpLicenseImgPath)

            if validateLicenseNumber(licenseNumber):
                predictions.append([score, licenseNumber, i])

        if not options["keep_tmp"]:
            shutil.rmtree(folder)

        predictions.sort(key=lambda record: record[0])
        if len(predictions) == 0 or predictions[-1][0] < options["ocr_threshold"]:
            print(f"INFO: DetectLicenseProcess: License number not detected.")
            packet.manualCheck = True
            op.put(packet)
            continue

        packet.licenseNumber = predictions[-1][1]
        packet.displayDo = track.journey[predictions[-1][2]]

        print(f"INFO: DetectLicenseProcess: License number: '{predictions[-1][1]}'.")
        op.put(packet)

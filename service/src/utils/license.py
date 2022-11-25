import uuid
import cv2
import os
import time

from src.utils.ocr import doOCR
from src.classes.detected_object import DetectedObject


def validateLicenseNumber(number):
    # TODO: Write validations
    return True


def detectLicense(ip, op, predictor, config):
    while True:
        if ip.empty():
            time.sleep(1)
            continue

        print(f"INFO: DetectLicenseProcess: Detecting license plate in image.")
        packet = ip.get()
        track = packet.track

        predictions = []
        for i, do in enumerate(track.journey):
            img = do.getCroppedImage()
            objData = predictor.getObjectsInImage(img)
            if len(objData) == 0:
                continue

            objData.sort(key=lambda record: record["score"])
            doLicensePlate = DetectedObject(img, objData[-1]["x1"], objData[-1]["x2"], objData[-1]["y1"], objData[-1]["y2"])

            tmpLicenseImgPath = f"tmp/{uuid.uuid4().hex}.jpg"
            cv2.imwrite(tmpLicenseImgPath, doLicensePlate.getCroppedImage())

            licenseNumber, score = doOCR(tmpLicenseImgPath)
            os.remove(tmpLicenseImgPath)

            if validateLicenseNumber(licenseNumber):
                predictions.append([score, licenseNumber, i])

        predictions.sort(key=lambda record: record[0])
        if len(predictions) == 0 or not validateLicenseNumber(predictions[-1][1]) and predictions[-1][0] >= config["ocr_threshold"]:
            print(f"INFO: DetectLicenseProcess: License number not detected.")
            packet.manualCheck = True
            op.put(packet)
            continue

        packet.licenseNumber = predictions[-1][1]
        packet.displayDo = track.journey[predictions[-1][2]]

        print(f"INFO: DetectLicenseProcess: License number: '{predictions[-1][1]}'.")
        op.put(packet)

import uuid
import cv2
import os

from src.utils.ocr import doOCR


def validateLicenseNumber(number):
    # TODO: Write validations
    return True


def detectLicense(ip, op, predictor):
    while True:
        if ip.empty():
            continue

        print(f"INFO: DetectLicenseProcess: Detecting license plate in image.")
        frame = ip.get()

        objData = predictor.getObjectsInImage(frame.img)
        objData.sort(key=lambda record: record["score"])

        if len(objData) > 0:
            data = objData[-1]
            img = data["img"]
            tmpLicenseImgPath = f"tmp/{uuid.uuid4().hex}.jpg"
            cv2.imwrite(tmpLicenseImgPath, img)

            licenseNumber = doOCR(tmpLicenseImgPath)
            os.remove(tmpLicenseImgPath)

            if validateLicenseNumber(licenseNumber):
                frame.licenseNumber = licenseNumber

        print(f"INFO: DetectLicenseProcess: License number: '{frame.licenseNumber}'.")
        op.put(frame)

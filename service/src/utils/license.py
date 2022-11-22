import uuid
import cv2
import os

from src.utils.ocr import doOCR


def detectLicense(ip, op, predictor):
    while True:
        if ip.empty():
            continue

        print(f"INFO: DetectLicenseProcess: Detecting license plate in image.")
        frame = ip.get()

        for data in predictor.getObjectsInImage(frame.img):
            img = data["img"]
            tmpLicenseImgPath = f"tmp/lp-{uuid.uuid4().hex}.jpg"
            cv2.imwrite(tmpLicenseImgPath, img)

            licenseNumber = doOCR(tmpLicenseImgPath)
            os.remove(tmpLicenseImgPath)

            # do this
            op.put(frame)

import uuid
import cv2
import json


def processResult(ip):
    while True:
        if ip.empty():
            continue

        print(f"INFO: ResultProcess: Generating result.")
        frame = ip.get()

        imgName = f"test_output/res-{uuid.uuid4().hex}.jpg"
        cv2.imwrite(imgName, frame.img)

        data = {
            "image_path": imgName,
            "owner": frame.vehicleOwner,
            "number": frame.licenseNumber
        }

        with open(f"test_output/{uuid.uuid4().hex}.json", "w") as f:
            json.dump(data, f)

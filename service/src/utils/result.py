import uuid
import cv2
import json
import requests


def processResult(ip, config):
    while True:
        if ip.empty():
            continue

        print(f"INFO: ResultProcess: Sending request.")
        frame = ip.get()

        payload = {
            "license_number": frame.licenseNumber,
            "image_url": "",
            "location": frame.location
        }

        print(payload)
        # resp = requests.post(config["challan_endpoint"], json=payload)
        # print(f"INFO: ResultProcess: Response: {resp}")

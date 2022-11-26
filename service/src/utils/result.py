import uuid
import cv2
import json
import requests
import os


def processResult(ip, config):
    while True:
        if ip.empty():
            continue

        print(f"INFO: ResultProcess: Sending request.")
        packet = ip.get()

        folder = f"media/{packet.track.id}"
        os.mkdir(folder)

        if packet.manualCheck:
            for idx, do in enumerate(packet.track.journey):
                cv2.imwrite(f"{folder}/{idx}.jpg", do.getCroppedImage())

        else:
            frame = packet.displayDo.getAnnotatedImage()
            cv2.imwrite(f"{folder}/frame.jpg", frame)
            vehicle = packet.displayDo.getCroppedImage()
            cv2.imwrite(f"{folder}/vehicle.jpg", vehicle)

        payload = {
            "license_number": packet.licenseNumber,
            "location": packet.location,
            "manual_check": packet.manualCheck,
            "folder": folder
        }

        print(payload)
        # resp = requests.post(config["challan_endpoint"], json=payload)
        # print(f"INFO: ResultProcess: Response: {resp}")

import uuid
import cv2
import json
import requests
import os
from collections import defaultdict


def makeChallan(config, licenseNumber, location, manualCheck, imageLocs):
    data = {
        "location": location,
        "license_number": licenseNumber,
        "status": "to_check_manually" if manualCheck else "unpaid",
    }
    response = requests.post(url=config["challan_endpoint"], data=data)
    new_challan_id = response.json()["id"]
    print(f"INFO: ResultProcess: Challan created.")

    for key in imageLocs:
        payload = {'challan': str(new_challan_id), 'type': key}
        for i, imageLoc in enumerate(imageLocs[key]):
            files = [('image', (f'{i}.jpg', open(imageLoc, 'rb'), 'image/jpeg'))]
            response = requests.post(config["challan_img_endpoint"], data=payload, files=files)

    print(f"INFO: ResultProcess: Images uploaded.")


def processResult(ip, config):
    while True:
        if ip.empty():
            continue

        print(f"INFO: ResultProcess: Sending request.")
        packet = ip.get()

        folder = f"tmp/result/{packet.track.id}"
        os.mkdir(folder)

        imageLocs = defaultdict(lambda: [])
        if packet.manualCheck:
            for idx, do in enumerate(packet.track.journey):
                cv2.imwrite(f"{folder}/{idx}.jpg", do.getCroppedImage())
                imageLocs["bulk"].append(f"{folder}/{idx}.jpg")

        else:
            frame = packet.displayDo.getAnnotatedImage()
            cv2.imwrite(f"{folder}/frame.jpg", frame)
            imageLocs["whole"].append(f"{folder}/frame.jpg")
            
            vehicle = packet.displayDo.getCroppedImage()
            cv2.imwrite(f"{folder}/vehicle.jpg", vehicle)
            imageLocs["cutout"].append(f"{folder}/vehicle.jpg")

        # print(packet.licenseNumber, packet.location, packet.manualCheck, imageLocs)
        try:
            makeChallan(config, packet.licenseNumber, packet.location, packet.manualCheck, imageLocs)
        except Exception as e:
            print(f"ERROR: ResultProcess: {e}.")

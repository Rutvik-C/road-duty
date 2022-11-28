import uuid
import cv2
import json
import requests
import os
from collections import defaultdict


def makeChallan(config, license_number, location, manual_check, image_locs):
    params = {"license_number": license_number}
    rider_info = requests.get(config["rider_endpoint"], params=params)
    print(f"rider {rider_info}")
    rider_info = rider_info.json()
    if rider_info == []:
        print(f"INFO: ResultProcess: Vehicle not registered.")
        return 

    rider_id = rider_info[0]['id']
    data = {
        "location": location,
        "license_number": license_number,
        "rider": rider_id,
        "status": "to_check_manually" if manual_check else "unpaid",
    }
    response = requests.post(url=config["challan_endpoint"], data=data)
    print("create", response)
    new_challan_id = response.json()["id"]
    print(f"INFO: ResultProcess: Challan created.")

    for key in image_locs:
        payload = {'challan': str(new_challan_id), 'type': key}
        for i, image_loc in enumerate(image_locs[key]):
            files = [('image', (f'{i}.jpg', open(image_loc, 'rb'), 'image/jpeg'))]
            response = requests.post(config["challan_img_endpoint"], data=payload, files=files)
            print("image", response)
    print(f"INFO: ResultProcess: Images uploaded.")


def processResult(ip, config):
    while True:
        if ip.empty():
            continue

        print(f"INFO: ResultProcess: Sending request.")
        packet = ip.get()

        folder = f"media/{packet.track.id}"
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

        try:
            makeChallan(config, packet.licenseNumber, packet.location, packet.manualCheck, imageLocs)
        except Exception as e:
            print(f"ERROR: ResultProcess: {e}.")

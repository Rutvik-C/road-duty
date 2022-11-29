import cv2
from multiprocessing import Queue, Process
import json
import time
import argparse
import os
from collections import deque

from src.classes.detector import Detector
from src.classes.packet import Packet

from src.utils.motorcycle import detectMotorcycle
from src.utils.helmet import detectHelmet
from src.utils.license import detectLicense
from src.utils.result import processResult

import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, required=True)
    parser.add_argument("--src", type=str, required=True)
    parser.add_argument("--address", type=str, required=True)
    parser.add_argument("--usePrecomputed", action="store_true")
    parser.add_argument("--precomputedSrc", type=str)
    parser.add_argument("--keepTmp", action="store_true")

    args = parser.parse_args()
    ipType = args.type
    ipSrc = args.src
    address = args.address
    usePrecomputed = args.usePrecomputed
    precomputedSrc = args.precomputedSrc
    keepTmp = args.keepTmp

    with open("config.json", "r") as f:
        config = json.load(f)

    motorcycleDetector, helmetDetector, licenseDetector = None, None, None
    if not usePrecomputed:
        motorcycleDetector = Detector("MotorcycleDetector", "models/motorcycle/v2/config.yaml", "models/motorcycle/v2/model_final.pth", 0.5)
        helmetDetector = Detector("HelmetDetector", "models/helmet/v1/config.yaml", "models/helmet/v1/model_final.pth", 0.5)
        licenseDetector = Detector("LicenseDetector", "models/license/v1/config.yaml", "models/license/v1/model_final.pth", 0.5)

    inputQueue = Queue()
    detectMotorcycleOutputQueue = Queue()
    detectHelmetOutputQueue = Queue()
    detectLicenseOutputQueue = Queue()

    motorcyclePrecomputed, helmetPrecomputed = [], []
    if usePrecomputed:
        with open(f"{precomputedSrc}/motorcycle.json", "r") as f:
            motorcyclePrecomputed = json.load(f)
        with open(f"{precomputedSrc}/helmet.json", "r") as f:
            helmetPrecomputed = json.load(f)

    motorcycleOptions = {
        "keep_tmp": keepTmp,
        "track": True if ipType == "video" else False,
        "detect": True if not usePrecomputed else False,
        "precomputed_data": motorcyclePrecomputed
    }
    helmetOptions = {
        "keep_tmp": keepTmp,
        "detect": True if not usePrecomputed else False,
        "precomputed_data": helmetPrecomputed
    }
    licenseOptions = {
        "keep_tmp": keepTmp,
        "ocr_threshold": config["ocr_threshold"]
    }
    resultOptions = {
        "keep_tmp": keepTmp,
        "challan_endpoint": config["challan_endpoint"],
        "challan_img_endpoint": config["challan_img_endpoint"]
    }
    
    Process(name="motorcycle", target=detectMotorcycle, args=(inputQueue, detectMotorcycleOutputQueue, motorcycleDetector, motorcycleOptions)).start()
    Process(name="helmet", target=detectHelmet, args=(detectMotorcycleOutputQueue, detectHelmetOutputQueue, helmetDetector, helmetOptions)).start()
    Process(name="license", target=detectLicense, args=(detectHelmetOutputQueue, detectLicenseOutputQueue, licenseDetector, licenseOptions)).start()
    Process(name="result", target=processResult, args=(detectLicenseOutputQueue, resultOptions)).start()

    print(f"INFO: Starting main loop.")
    if ipType == "video":
        print(f"INFO: Reading {ipSrc}")
        cap = cv2.VideoCapture(ipSrc)
        
        count = 0
        FRAME = 1
        while cap.isOpened():
            ret, frame = cap.read()
            if count % FRAME == 0:
                if ret:
                    imgLoc = f"tmp/motorcycle_queue/{count}.jpg"
                    cv2.imwrite(imgLoc, frame)
                    inputQueue.put(Packet(count, imgLoc, address))
                    count += 1
        
        while True:
            time.sleep(10)
    
    elif ipType == "image":
        images = deque()
        for file in os.listdir(ipSrc):
            print(f"INFO: Reading {ipSrc}/{file}")
            images.append(f"{ipSrc}/{file}")

        count = 0
        while True:
            if len(images) > 0:
                imgLoc = images.popleft()
                inputQueue.put(Packet(count, imgLoc, address))
                count += 1
            else:
                time.sleep(10)

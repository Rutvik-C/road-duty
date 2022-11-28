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

    args = parser.parse_args()
    ipType = args.type
    ipSrc = args.src
    address = args.address
    detect = args.usePrecomputed
    precomputedSrc = args.precomputedSrc

    with open("config.json", "r") as f:
        config = json.load(f)

    motorcycleDetector = Detector("MotorcycleDetector", "models/motorcycle/v2/config.yaml", "models/motorcycle/v2/model_final.pth", 0.5)
    helmetDetector = Detector("HelmetDetector", "models/helmet/v1/config.yaml", "models/helmet/v1/model_final.pth", 0.5)
    licenseDetector = Detector("LicenseDetector", "models/license/v1/config.yaml", "models/license/v1/model_final.pth", 0.5)

    inputQueue = Queue()
    detectMotorcycleOutputQueue = Queue()
    detectHelmetOutputQueue = Queue()
    detectLicenseOutputQueue = Queue()

    motorcycleOptions = {
        "track": False if ipType == "image" else True,
        "detect": True
    }

    Process(name="motorcycle", target=detectMotorcycle, args=(inputQueue, detectMotorcycleOutputQueue, motorcycleDetector, motorcycleOptions)).start()
    Process(name="helmet", target=detectHelmet, args=(detectMotorcycleOutputQueue, detectHelmetOutputQueue, helmetDetector)).start()
    Process(name="license", target=detectLicense, args=(detectHelmetOutputQueue, detectLicenseOutputQueue, licenseDetector, config)).start()
    Process(name="result", target=processResult, args=(detectLicenseOutputQueue, config)).start()

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
                    inputQueue.put(Packet(count, frame, address))
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
                frame = Packet(count, cv2.imread(images.popleft()), address)
                inputQueue.put(frame)
                count += 1
            else:
                time.sleep(10)

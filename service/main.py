import cv2
from multiprocessing import Queue, Process
import json
import time
import argparse

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

    args = parser.parse_args()
    ipType = args.type
    ipSrc = args.src

    with open("config.json", "r") as f:
        config = json.load(f)

    motorcycleDetector = Detector("MotorcycleDetector", "models/motorcycle/v2/config.yaml", "models/motorcycle/v2/model_final.pth", 0.5)
    helmetDetector = Detector("HelmetDetector", "models/helmet/v1/config.yaml", "models/helmet/v1/model_final.pth", 0.5)
    licenseDetector = Detector("LicenseDetector", "models/license/v1/config.yaml", "models/license/v1/model_final.pth", 0.5)

    inputQueue = Queue()
    detectMotorcycleOutputQueue = Queue()
    detectHelmetOutputQueue = Queue()
    detectLicenseOutputQueue = Queue()

    with open("test_output/test4.json", "r") as f:
        data = json.load(f)

    motorcycleOptions = {
        "track": False,
        "detect": True,
        "object_data": data
    }

    Process(name="motorcycle", target=detectMotorcycle, args=(inputQueue, detectMotorcycleOutputQueue, motorcycleDetector, motorcycleOptions)).start()
    Process(name="helmet", target=detectHelmet, args=(detectMotorcycleOutputQueue, detectHelmetOutputQueue, helmetDetector)).start()
    Process(name="license", target=detectLicense, args=(detectHelmetOutputQueue, detectLicenseOutputQueue, licenseDetector, config)).start()
    Process(name="result", target=processResult, args=(detectLicenseOutputQueue, config)).start()

    tmp = ["test/252_e.jpg"]

    print(f"INFO: Starting main loop.")
    while True:
        if len(tmp) > 0:
            frame = Packet(len(tmp), cv2.imread(tmp.pop()), "Nanodiwadi Vasalai")
            inputQueue.put(frame)

        time.sleep(10)

    # cap = cv2.VideoCapture("test/demo4.mp4")
    #
    # count = 0
    # FRAME = 1
    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     if count % FRAME == 0:
    #         if ret:
    #             inputQueue.put(Packet(count, frame, ""))
    #
    #     count += 1
    #
    # print("Dead loop")
    # while True:
    #     pass

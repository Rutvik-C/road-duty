import cv2
from multiprocessing import Queue, Process
import json

from src.classes.detector import Detector
from src.classes.frame import Frame

from src.utils.motorcycle import detectMotorcycle
from src.utils.helmet import detectHelmet
from src.utils.license import detectLicense
from src.utils.result import processResult


if __name__ == '__main__':
    with open("config.json", "r") as f:
        config = json.load(f)

    motorcycleDetector = Detector("MotorcycleDetector", "models/motorcycle/v2/config.yaml", "models/motorcycle/v2/model_final.pth", 0.5)
    helmetDetector = Detector("HelmetDetector", "models/helmet/v1/config.yaml", "models/helmet/v1/model_final.pth", 0.5)
    licenseDetector = Detector("LicenseDetector", "models/license/v1/config.yaml", "models/license/v1/model_final.pth", 0.5)

    inputQueue = Queue()
    detectMotorcycleOutputQueue = Queue()
    detectHelmetOutputQueue = Queue()
    detectLicenseOutputQueue = Queue()

    Process(target=detectMotorcycle, args=(inputQueue, detectMotorcycleOutputQueue, motorcycleDetector)).start()
    Process(target=detectHelmet, args=(detectMotorcycleOutputQueue, detectHelmetOutputQueue, helmetDetector)).start()
    Process(target=detectLicense, args=(detectHelmetOutputQueue, detectLicenseOutputQueue, licenseDetector)).start()
    Process(target=processResult, args=(detectLicenseOutputQueue, config)).start()

    tmp = ["test/299.jpg"]

    print(f"INFO: Starting main loop.")
    while True:
        if len(tmp) > 0:
            frame = Frame(cv2.imread(tmp.pop()), "Nanodiwadi Vasalai")
            inputQueue.put(frame)

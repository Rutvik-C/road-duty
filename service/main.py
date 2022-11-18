import cv2
from multiprocessing import Queue, Process

from src.classes.detector import Detector
from src.utils.motorcycle import detectMotorcycle
from src.utils.helmet import detectHelmet
from src.utils.license import detectLicense
from src.utils.result import processResult


if __name__ == '__main__':
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
    Process(target=processResult, args=(detectLicenseOutputQueue,)).start()

    tmp = ["test/332.jpg"]

    print(f"INFO: Starting main loop.")
    while True:
        if len(tmp) > 0:
            inputQueue.put(cv2.imread(tmp.pop()))

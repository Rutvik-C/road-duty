import detectron2
import torch
import cv2
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer
from multiprocessing import Queue, Process
import time

from src.classes.detector import Detector
from src.utils.motorcycle import detectMotorcycle
from src.utils.helmet import detectHelmet


if __name__ == '__main__':
    motorcycleDetector = Detector("models/motorcycle/v2/config.yaml", "models/motorcycle/v2/model_final.pth", 0.5)
    helmetDetector = Detector("models/helmet/v1/config.yaml", "models/helmet/v1/model_final.pth", 0.5)

    inputQueue = Queue()
    detectMotorcycleOutputQueue = Queue()
    detectHelmetOutputQueue = Queue()

    Process(target=detectMotorcycle, args=(inputQueue, detectMotorcycleOutputQueue, motorcycleDetector)).start()
    Process(target=detectHelmet, args=(detectMotorcycleOutputQueue, detectHelmetOutputQueue, helmetDetector)).start()



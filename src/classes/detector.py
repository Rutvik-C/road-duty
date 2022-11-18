import logging
import detectron2
import torch
import cv2
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor


class Detector:
    def __init__(self, configFile, weightsFile, threshold=0.6):
        self.configFile = configFile
        self.weightsFile = weightsFile
        self.threshold = threshold
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"INFO: Using device '{self.device}'.")
        self.predictor = self.getPredictor()

    def getConfig(self):
        print("INFO: Setting up configs.")
        cfg = get_cfg()
        cfg.merge_from_file(self.configFile)
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = self.threshold
        cfg.MODEL.WEIGHTS = self.weightsFile
        cfg.MODEL.DEVICE = self.device

        return cfg

    def getPredictor(self):
        print("INFO: Setting up predictor.")
        return DefaultPredictor(self.getConfig())

    def getOutput(self, img):
        print("INFO: Detecting objects")
        return self.predictor(img)

    def getObjectsInImage(self, img):
        outputs = self.getOutput(img)

        print("INFO: Extracting objects in image.")
        boxes = outputs["instances"].get_fields()["pred_boxes"]
        scores = outputs["instances"].get_fields()["scores"]
        pclasses = outputs["instances"].get_fields()["pred_classes"]
        data = []

        for box, score, pclass in zip(boxes, scores, pclasses):
            tmp = {
                "img": img[int(box[1]): int(box[3]), int(box[0]): int(box[2])],
                "score": score,
                "class": pclass
            }
            data.append(tmp)

        return data

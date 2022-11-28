import torch
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor


class Detector:
    def __init__(self, name, configFile, weightsFile, threshold=0.6):
        self.name = name
        self.configFile = configFile
        self.weightsFile = weightsFile
        self.threshold = threshold
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"INFO: {self.name}: Using device '{self.device}'.")
        self.predictor = self.getPredictor()

    def getConfig(self):
        print(f"INFO: {self.name}: Setting up configs.")
        cfg = get_cfg()
        cfg.merge_from_file(self.configFile)
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = self.threshold
        cfg.MODEL.WEIGHTS = self.weightsFile
        cfg.MODEL.DEVICE = self.device

        return cfg

    def getPredictor(self):
        print(f"INFO: {self.name}: Setting up predictor.")
        return DefaultPredictor(self.getConfig())

    def getOutput(self, img):
        print(f"INFO: {self.name}: Detecting objects.")
        return self.predictor(img)

    def getObjectsInImage(self, img):
        outputs = self.getOutput(img)

        boxes = outputs["instances"].get_fields()["pred_boxes"]
        scores = outputs["instances"].get_fields()["scores"]
        pclasses = outputs["instances"].get_fields()["pred_classes"]
        data = []

        for box, score, pclass in zip(boxes, scores, pclasses):
            tmp = {
                "score": score,
                "class": pclass,
                "x1": int(box[0]),
                "x2": int(box[2]),
                "y1": int(box[1]),
                "y2": int(box[3]),
            }
            data.append(tmp)

        print(f"INFO: {self.name}: Extracted {len(data)} objects.")
        return data

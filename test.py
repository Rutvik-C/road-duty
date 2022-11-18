import detectron2
import torch
import cv2
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer
from src.classes.detector import Detector


motorcycleDetector = Detector("models/motorcycle/v2/config.yaml", "models/motorcycle/v2/model_final.pth", 0.5)

img = cv2.imread("test/332.jpg")

# v = Visualizer(
#     img[:, :, ::-1],
#     scale=0.8,
# )
# v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
# cv2.imwrite("test.jpg", v.get_image()[:, :, :: -1])

c = 0
for data in motorcycleDetector.getObjectsInImage(img):
    cv2.imwrite(f"output/img{c}-score{data['score']}-class{data['class']}.jpg", data["img"])
    c += 1

print("Complete.")
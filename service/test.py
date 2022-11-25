from src.classes.detected_object import DetectedObject

import json
import cv2


do = DetectedObject(cv2.imread("test/1.png"), 626, 833, 309, 706)
print(do.getWidth())
print(do.getHeight())
cv2.imwrite("test_output/out.jpg", do.getCroppedImage())
print("Complete")

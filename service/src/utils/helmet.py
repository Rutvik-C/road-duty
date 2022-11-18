import uuid
import cv2


def detectHelmet(ip, op, detector):
    while True:
        if ip.empty():
            continue

        print(f"INFO: DetectHelmetProcess: Detecting helmet in image.")
        img = ip.get()

        cv2.imwrite(f"test_output/s1-{uuid.uuid4().hex}.jpg", img)

        for data in detector.getObjectsInImage(img):
            if data["class"] == 1:
                op.put(img)

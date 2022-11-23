import uuid
import cv2


def detectHelmet(ip, op, detector):
    while True:
        if ip.empty():
            continue

        print(f"INFO: DetectHelmetProcess: Detecting helmet in image.")
        frame = ip.get()

        count = 0
        for data in detector.getObjectsInImage(frame.img):
            if data["class"] == 0:
                count += 1

        print(f"INFO: DetectHelmetProcess: Detected {count} helmets.")
        if count == 0:
            op.put(frame)

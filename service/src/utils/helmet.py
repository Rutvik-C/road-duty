import uuid
import cv2


def detectHelmet(ip, op, detector):
    while True:
        if ip.empty():
            continue

        print(f"INFO: DetectHelmetProcess: Detecting helmet in image.")
        frame = ip.get()

        cv2.imwrite(f"test_output/hel-{uuid.uuid4().hex}.jpg", frame.img)

        for data in detector.getObjectsInImage(frame.img):
            if data["class"] == 1:
                op.put(frame)
                break

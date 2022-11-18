import uuid
import cv2


def processResult(ip):
    while True:
        if ip.empty():
            continue

        print(f"INFO: ResultProcess: Generating result.")
        img = ip.get()

        cv2.imwrite(f"test_output/s2-{uuid.uuid4().hex}.jpg", img)

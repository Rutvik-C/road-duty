import uuid
import cv2
import time


def detectHelmet(ip, op, detector):
    while True:
        if ip.empty():
            time.sleep(1)
            continue

        print(f"INFO: DetectHelmetProcess: Detecting helmet in image.")
        packet = ip.get()
        track = packet.track

        total, positive = 0, 0
        for do in track.journey:
            objData = detector.getObjectsInImage(do.getCroppedImage())

            count = 0
            for data in objData:
                if data["class"] == 0:
                    count += 1

            if count == 0:
                positive += 1
            total += 1

        print(f"INFO: DetectHelmetProcess: Helmet not found in {positive}/{total} instances.")
        if positive >= 0.75 * total:
            op.put(packet)

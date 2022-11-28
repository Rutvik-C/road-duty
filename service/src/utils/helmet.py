import uuid
import cv2
import time


def detectHelmet(ip, op, detector, options):
    while True:
        if ip.empty():
            time.sleep(1)
            continue

        packet = ip.get()
        track = packet.track
        print(f"INFO: DetectHelmetProcess: Detecting helmet in track {track.id}.")

        total, positive = 0, 0
        for idx, do in enumerate(track.journey):
            objData = detector.getObjectsInImage(do.getCroppedImage()) if options["detect"] else options["precomputed_data"][str(track.id)][idx]

            count = 0
            for data in objData:
                if data["class"] == 0:
                    count += 1

            if count == 0:
                positive += 1
            total += 1

        print(f"INFO: DetectHelmetProcess: Violation in {positive}/{total} instances.")
        if positive >= 0.75 * total:
            print(f"Hey Hey. Sending packet {track.id} to next")
            # op.put(packet)

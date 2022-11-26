import time
import os
import cv2

from src.classes.track import Track
from src.classes.packet import Packet
from src.classes.detected_object import DetectedObject


def detectMotorcycle(ip, op, detector, options):
    tracks = []

    while True:
        if ip.empty():
            time.sleep(1)
            continue

        print(f"INFO: DetectMotorcycleProcess: Detecting motorcycle in image.")
        packet = ip.get()
        trackWithSuccessor = {}

        objData = detector.getObjectsInImage(packet.img) if options["detect"] else options["object_data"][packet.id]["objects"]
        for data in objData:
            do = DetectedObject(packet.img, data["x1"], data["x2"], data["y1"], data["y2"])
            centerX = (do.x1 + do.x2) // 2
            centerY = (do.y1 + do.y2) // 2

            if not options["track"]:
                newTrack = Track()
                newTrack.addTrackFragment(centerX, centerY, do)
                op.put(Packet(-1, packet.img, packet.location, newTrack))
                continue

            isInVicinity = False
            for track in tracks:
                print(f"Track centered at {track.x}, {track.y} with rx={track.rx} ry={track.ry}")

                if track.id not in trackWithSuccessor and track.isClose(centerX, centerY):
                    print(f"{track.id} is close. Adding to existing")
                    track.addTrackFragment(centerX, centerY, do)
                    isInVicinity = True
                    trackWithSuccessor[track.id] = True
                    break

            if not isInVicinity:
                newTrack = Track()
                newTrack.addTrackFragment(centerX, centerY, do)
                tracks.append(newTrack)
                trackWithSuccessor[newTrack.id] = True

                print(f"Not in vicinity. Creating new track {newTrack.id}")
            print("-" * 30)

        if options["track"]:
            i = 0
            while i < len(tracks):
                if tracks[i].id not in trackWithSuccessor:
                    print(f"Journey of {tracks[i].id} ended")
                    if tracks[i].isValid():
                        op.put(Packet(-1, packet.img, packet.location, tracks[i]))

                    # os.mkdir(f"test_output/{tracks[i].id}")
                    # for idx, img in enumerate(tracks[i].journey):
                    #     cv2.imwrite(f"test_output/{tracks[i].id}/{idx}.jpg", img)

                    del tracks[i]

                i += 1


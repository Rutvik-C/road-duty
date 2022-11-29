import time
import os
import cv2

from src.classes.track import Track
from src.classes.packet import Packet
from src.classes.detected_object import DetectedObject


def detectMotorcycle(ip, op, detector, options):
    print(f"INFO: DetectMotorcycleProcess: detect={options['detect']}, track={options['track']}")
    tracks = []
    trackCount = 0

    while True:
        if ip.empty():
            time.sleep(1)
            continue

        print(f"INFO: DetectMotorcycleProcess: Detecting motorcycle in image.")
        packet = ip.get()
        trackWithSuccessor = {}

        objData = detector.getObjectsInImage(cv2.imread(packet.imgLoc)) if options["detect"] else options["precomputed_data"][packet.frameId]
        for data in objData:
            do = DetectedObject(packet.imgLoc, data["x1"], data["x2"], data["y1"], data["y2"])
            centerX = (do.x1 + do.x2) // 2
            centerY = (do.y1 + do.y2) // 2

            if not options["track"]:
                newTrack = Track(trackCount)
                newTrack.addTrackFragment(centerX, centerY, do)
                op.put(Packet(-1, packet.imgLoc, packet.location, newTrack))
                trackCount += 1
                continue

            isInVicinity = False
            for track in tracks:
                if track.id not in trackWithSuccessor and track.isClose(centerX, centerY):
                    print(f"INFO: DetectMotorcycleProcess: {track.id} is close. Adding to existing")
                    track.addTrackFragment(centerX, centerY, do)
                    isInVicinity = True
                    trackWithSuccessor[track.id] = True
                    break

            if not isInVicinity:
                newTrack = Track(trackCount)
                newTrack.addTrackFragment(centerX, centerY, do)
                tracks.append(newTrack)
                trackWithSuccessor[newTrack.id] = True
                trackCount += 1
                print(f"INFO: DetectMotorcycleProcess: Not in vicinity. Creating new track {newTrack.id}")

        if options["track"]:
            i = 0
            while i < len(tracks):
                if tracks[i].id not in trackWithSuccessor:
                    print(f"INFO: DetectMotorcycleProcess: Journey of {tracks[i].id} ended")
                    if tracks[i].isValid():
                        op.put(Packet(-1, packet.imgLoc, packet.location, tracks[i]))

                        folder = f"tmp/tracks/{tracks[i].id}"
                        os.mkdir(folder)
                        for idx, do in enumerate(tracks[i].journey):
                            cv2.imwrite(f"{folder}/{idx}.jpg", do.getCroppedImage())

                    del tracks[i]
                i += 1

from src.classes.frame import Frame


def detectMotorcycle(ip, op, detector):
    while True:
        if ip.empty():
            continue

        print(f"INFO: DetectMotorcycleProcess: Detecting motorcycle in image.")
        frame = ip.get()

        objData = detector.getObjectsInImage(frame.img)
        for data in objData:
            newFrame = Frame(data["img"], frame.location)
            op.put(newFrame)

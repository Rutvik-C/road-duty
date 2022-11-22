from src.classes.frame import Frame


def detectMotorcycle(ip, op, detector):
    while True:
        if ip.empty():
            continue

        print(f"INFO: DetectMotorcycleProcess: Detecting motorcycle in image.")
        frame = ip.get()

        for data in detector.getObjectsInImage(frame.img):
            op.put(Frame(data["img"], frame.location))

def detectMotorcycle(ip, op, detector):
    while True:
        if ip.empty():
            continue

        print(f"INFO: DetectMotorcycleProcess: Detecting motorcycle in image.")
        img = ip.get()

        for data in detector.getObjectsInImage(img):
            op.put(data["img"])

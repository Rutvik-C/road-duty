import time


def detectMotorcycle(ip, op, detector):
    while True:
        if ip.empty():
            time.sleep(1)
            continue

        print(f"INFO: detectMotorcycle: detecting motorcycle in image.")
        img = ip.get()

        for data in detector.getObjectsInImage(img):
            op.put(data["img"])

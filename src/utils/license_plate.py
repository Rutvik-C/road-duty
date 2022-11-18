import time


def detectLicense(ip, op, predictor):
    while True:
        if ip.empty():
            time.sleep(1)
            continue

        print(f"INFO: detectMotorcycle: detecting license plate in image.")
        img = ip.get()

import time


def detectHelmet(ip, op, predictor):
    while True:
        if ip.empty():
            time.sleep(1)
            continue

        print(f"INFO: detectMotorcycle: detecting helmet in image.")
        img = ip.get()

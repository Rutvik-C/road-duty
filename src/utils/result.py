import time


def processResult(ip):
    while True:
        if ip.empty():
            time.sleep(1)
            continue

        print(f"INFO: detectMotorcycle: generating result.")
        img = ip.get()

def detectLicense(ip, op, predictor):
    while True:
        if ip.empty():
            continue

        print(f"INFO: DetectLicenseProcess: Detecting license plate in image.")
        img = ip.get()

        for data in predictor.getObjectsInImage(img):
            op.put(data["img"])

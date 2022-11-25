class Packet:
    def __init__(self, frameId, img, location, track=None):
        self.frameId = frameId
        self.img = img
        self.track = track

        self.location = location

        self.licenseNumber = None
        self.displayDo = None
        self.manualCheck = False

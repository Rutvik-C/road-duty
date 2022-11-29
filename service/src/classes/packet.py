class Packet:
    def __init__(self, frameId, imgLoc, location, track=None):
        self.frameId = frameId
        self.imgLoc = imgLoc
        self.track = track

        self.location = location

        self.licenseNumber = None
        self.displayDo = None
        self.manualCheck = False

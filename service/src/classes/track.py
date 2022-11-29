import json
import uuid


class Track:
    def __init__(self, idx):
        self.id = idx  # uuid.uuid4().hex
        self.x = 0
        self.y = 0
        self.journey = []
        self.rx = 0
        self.ry = 0
        
        with open("config.json", "r") as f:
            config = json.load(f)
            self.slideMarginX = config["slide_margin_x"]
            self.slideMarginY = config["slide_margin_y"]

    def addTrackFragment(self, x, y, do):
        self.x = x
        self.y = y
        self.journey.append(do)

        self.rx = self.slideMarginX * do.getWidth()
        self.ry = self.slideMarginY * do.getHeight()

    def isClose(self, x, y):
        return self.x - self.rx <= x <= self.x + self.rx and self.y - self.ry <= y <= self.y + self.ry

    def isValid(self):
        return len(self.journey) > 5

import cv2


class DetectedObject:
    def __init__(self, imgLoc, x1, x2, y1, y2):
        self.imgLoc = imgLoc
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def getHeight(self):
        return abs(self.y1 - self.y2)

    def getWidth(self):
        return abs(self.x1 - self.x2)

    def getCroppedImage(self):
        img = cv2.imread(self.imgLoc)
        return img[self.y1: self.y2, self.x1: self.x2]

    def getAnnotatedImage(self):
        img = cv2.imread(self.imgLoc)
        return cv2.rectangle(img, (self.x1, self.y1), (self.x2, self.y2), (0, 0, 255), 2)

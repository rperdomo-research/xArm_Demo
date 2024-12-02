import pyrealsense2 as rs
import numpy as np
import cv2

class CamUtil:
    def __init__(self):
        # setup cam
        pass

    def __detectPoints(self):
        return np.array()
        pass

    def calibrateCamera(self, pixelList, IRLDist):
        _IRLpoints = np.array([[0, 0], [0, 16.375], [21.25, 0]])
        pixelList = self.__detectPoints().sort()
        H, mask = cv2.findHomography(pixelList, _IRLpoints, cv2.RANSAC, 5.0)
        return H
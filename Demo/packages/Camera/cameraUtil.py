import pyrealsense2 as rs
import numpy as np
import cv2
import time

class CamUtil:
    def __init__(self):
        # setup cam
        self.pipeline = rs.pipeline()
        self.config = rs.config()

        pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
        pipeline_profile = self.config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device()
        device_product_line = str(device.get_info(rs.camera_info.product_line))

        found_rgb = False
        for s in device.sensors:
            if s.get_info(rs.camera_info.name) == 'RGB Camera':
                found_rgb = True
                break
        if not found_rgb:
            print("The demo requires Depth camera with Color sensor")
            exit(0)

        #self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        # Start streaming
        self.pipeline.start(self.config)


        frames = self.pipeline.wait_for_frames()

        color_frame = frames.get_color_frame()
        if color_frame:
            color_image = np.asanyarray(color_frame.get_data())
            color_colormap_dim = color_image.shape

            cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('RealSense', color_image)
            time.sleep(5)
        pass

    def __detectPoints(self):
        return np.array()
        pass

    def calibrateCamera(self, pixelList, IRLDist):
        _IRLpoints = np.array([[0, 0], [0, 16.375], [21.25, 0]])
        pixelList = self.__detectPoints().sort()
        H, mask = cv2.findHomography(pixelList, _IRLpoints, cv2.RANSAC, 5.0)
        return H
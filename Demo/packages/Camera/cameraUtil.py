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
        

    def __detectPoints(self):
        corn = []
        
        marker = cv2.imread("C:/Users/robotpc/Desktop/Research/xArm_Demo/Demo/testStuff/sceneAruco2.PNG")

        #cv2.imshow("Marker", marker)
        #cv2.waitKey(2000)

        gray = cv2.cvtColor(marker.copy(), cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        #cv2.imshow("thresh", thresh)
        #cv2.waitKey(5000)

        aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_1000)
        param = cv2.aruco.DetectorParameters()

        detector = cv2.aruco.ArucoDetector(aruco_dict, param)

        corners, ids, rejected = detector.detectMarkers(thresh)

        print("Detected markers: ", ids)
        if ids is not None:
            for markerCorners in corners:
                print(markerCorners)
                topleft, topright, bottomright, bottomleft = markerCorners[0]

                center_x = int((topleft[0]+bottomright[0]) / 2)
                center_y = int((topleft[1]+bottomright[1]) / 2)
                print("{}, {}".format(center_x, center_y))
                cv2.circle(marker, (center_x, center_y), 5, (0, 0, 255), -1)
                corn.append([center_x, center_y])

            #cv2.imshow("Detected", marker)
            #cv2.waitKey(5000)
        
        return np.array(corn)

    def detectObject(self):
        # returns object center and robot location
        #rl = [img.shape[0]/2, 1]
        pass

    def calibrateCamera(self):
        _IRLpoints = np.array([[0, 0], [0, 16.375], [21.25, 0]])
        pixelList = self.__detectPoints() #.sort()
        print("pixelList: {}".format(pixelList))
        H, mask = cv2.findHomography(pixelList, _IRLpoints, cv2.RANSAC, 5.0)
        return H
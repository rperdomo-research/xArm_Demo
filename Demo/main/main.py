import sys
sys.path.insert(0, 'C:\\Users\\robotpc\\Desktop\\Research\\xArm_Demo\\Demo')

from packages.FTPython import RFT_UART as ft # type: ignore
from packages.MovementFiles import movexArm as mv # type: ignore
from packages.Camera import cameraUtil as cu # type: ignore
from packages.MovementFiles import positions as ps # type: ignore


import pyrealsense2 as rs
import numpy as np
import cv2

def main():

    robot = mv.Arm("192.168.1.224") #connect to robot via address
    #force = ft.RFTseries(port="COM3")
    #camera = cu.CamUtil()
    #H_matrix = calibrate(robot, camera)

    # detect block
    # returns center point and scene center (robot location)

    # rotate to block
    # turnToObject(center, vector) # <- vector from center point 


    print("Hello")

    robot.limitTest([90, 0, -135, 135, 180, 0])

    print("Done")



    #obot.reset()
    robot.endArmUsage() #disconnect from robot

def calibrate(robo, cam):
    # move to calibration zone
    robo.goToCalibrationZone()
    # call calibration function
    # return homography matrix
    return cam.calibrateCamera()
    

if __name__ == "__main__":
    main()
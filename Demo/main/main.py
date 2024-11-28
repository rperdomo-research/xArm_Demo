import sys
sys.path.insert(0, 'C:\\Users\\robotpc\\Desktop\\Research\\xArm_Demo\\Demo')

from packages.FTPython import RFT_UART as ft # type: ignore
from packages.MovementFiles import movexArm as mv # type: ignore

import pyrealsense2 as rs
import numpy as np
import cv2

def main():

    robot = mv.Arm("192.168.1.224") #connect to robot via address
    #force = ft.RFTseries(port="COM3")


    print("Hello")

    robot.limitTest([90, 0, 0, 0, 0, 0])

    print("Done")



    robot.reset()
    robot.endArmUsage() #disconnect from robot

if __name__ == "__main__":
    main()
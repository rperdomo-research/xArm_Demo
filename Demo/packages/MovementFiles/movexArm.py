from xarm.wrapper import XArmAPI

'''
1 - shoulder rotation
2 - shoulder? angle
3 - elbow angle
4 - wrist angle
5 - wrist rotation
6 - i think end effector action
'''

class Arm:
    def __init__(self, ip):
        """
        Remember to power on the xArm
        """
        self.arm = XArmAPI(ip)

        self.arm.motion_enable(enable=True)
        self.arm.set_mode(0)
        self.arm.set_state(state=0)

        self.arm.reset(wait=True)

        self.speed = 50

    def limitTest(self, position):
        self.arm.set_servo_angle(angle=position, speed=self.speed, wait=True)

    def goToStart(self):
        self.arm.set_servo_angle(angle=[90, -30, -45, 75, 0, 0], speed=self.speed, wait=True)
        #print(arm.get_servo_angle(), arm.get_servo_angle(is_radian=True))
        pass

    def goToEnd(self):
        pass

    def grabObject(self):
        pass

    def reset(self):
        self.arm.reset(wait=True)

    def enableArm(self):
        self.arm.motion_enable(enable=True)

    def disableArm(self):
        self.arm.motion_enable(enable=False)

    def endArmUsage(self):
        self.arm.disconnect()
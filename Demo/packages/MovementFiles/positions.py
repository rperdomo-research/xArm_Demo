'''
1 - shoulder rotation
2 - shoulder? angle
3 - elbow angle
4 - wrist angle
5 - wrist rotation
6 - i think end effector action
'''

SR_LowerLimit = 45
SR_UpperLimit = 135

SA_LowerLimit = -90
SA_UpperLimit = 20

EA_LowerLimit = -180
EA_UpperLimit = 0

WA_LowerLimit = 0
WA_UpperLimit = 90

WR_LowerLimit = -90
WR_UpperLimit = 90

EE_LowerLimit = 0
EE_UpperLimit = 0


GOTO_START = []
GOTO_END = []
GRAB = []
LETGO = []
UPRIGHT = [90, 0, -180, 0, 0, 0]
CAMERA_CALIBRATE = [90, 0, -135, 135, 0, 0] # rotate wrist 180 until new adapter made
WORK_ON_END_EFFECTOR = []
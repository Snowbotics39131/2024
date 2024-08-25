from PortMap24 import *

driveBase.straight(1000)
driveBase.turn(30)
#motorBack.run_angle(1000, 360)
#motorFront.run_angle(1000, 360)
driveBase.straight(50)
driveBase.turn(-30)
driveBase.straight(50)
motorFront.run_angle(1000, 90)
motorFront.run_angle(1000, -90)
driveBase.straight(-100)
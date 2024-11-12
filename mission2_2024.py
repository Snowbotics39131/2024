from PortMap24 import * 
#1,4
driveBase.settings(straight_speed=600)
driveBase.settings(turn_rate=100)
wait(100)
driveBase.turn(-17)
driveBase.straight(750)
driveBase.straight(-200)
driveBase.turn(17)
driveBase.straight(1000)
driveBase.turn(45)
driveBase.straight(-300)
driveBase.straight(600)
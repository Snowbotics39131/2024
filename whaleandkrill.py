from PortMap24 import *
#2nd thick black line from outside allighn to outside. 
driveBase.settings(turn_rate=40)
driveBase.straight(100)
driveBase.turn(-35)
driveBase.straight(400)
driveBase.turn(65)
driveBase.straight(200)
#driveBase.turn(-60)
#driveBase.straight(150)
#wait(2)
driveBase.turn(14)
#driveBase.straight(120)
wait(60)
#driveBase.settings(straight_speed=40)
driveBase.straight(200)
driveBase.settings(straight_speed=40)
#driveBase.turn()
driveBase.straight(-50)
driveBase.settings(straight_speed=300)
driveBase.settings(turn_rate=100)
driveBase.curve(-400,90)

driveBase.straight(-250)
#driveBase.turn(-50)
#driveBase.straight(-350)
#driveBase.turn(-35)
#driveBase.straight(-350)

from PortMap24 import *
print(driveBase.settings())
motorFront.run_until_stalled(1000,Stop.COAST,30)
driveBase.settings(150,300,150,300)
driveBase.turn(-35)
driveBase.straight(290)
driveBase.turn(85)
driveBase.straight(180)
motorFront.run_angle(1000, -290)
driveBase.straight(-100)
motorFront.run_angle(1000, 110)
driveBase.turn(-55)
driveBase.settings(straight_speed=500)
driveBase.straight(-350)
driveBase.use_gyro(False)
driveBase.straight(-200)
driveBase.use_gyro(True)
#driveBase.turn(35)
#motorFront.run_angle(1000, -180)
driveBase.settings(straight_speed=-300)
driveBase.straight(400)
driveBase.turn(-15)
driveBase.straight(100)
driveBase.turn(15)
driveBase.straight(300)
driveBase.use_gyro(False)
driveBase.straight(190)
driveBase.use_gyro(True)
driveBase.straight(-200)
#motorFront.run_angle(1000, 160)
#driveBase.straight(-300)
#driveBase.straight(-180)
driveBase.settings(straight_speed=500)
driveBase.turn(60)
driveBase.straight(200)
driveBase.straight(-150)
driveBase.turn(-80)
driveBase.straight(-700)
#driveBase.turn(-45)
#driveBase.straight(-400)
motorFront.run_angle(1000, 130)
#driveBase.curve(600,-90)
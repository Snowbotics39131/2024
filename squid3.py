from PortMap24 import * 
#8,0
timer = StopWatch()
timer.reset()
async def downUp(height):
    await motorFront.run_until_stalled(-1000,Stop.COAST,30)
    await motorFront.run_angle(500,height)
async def lockDriveAndlift(distance,height):
    await multitask(driveBase.straight(distance),downUp(height))

async def driveAndlift(distance,height):
    await multitask(driveBase.straight(distance),motorFront.run_angle(500,height))
    
driveBase.use_gyro(True)
print(driveBase.settings())
driveBase.settings(turn_acceleration=200)
driveBase.settings(straight_acceleration=200)
driveBase.settings(straight_speed=155)
driveBase.settings(turn_rate=65)
run_task(lockDriveAndlift(-550,160))
#motorFront.run_until_stalled(-1000,Stop.COAST,30)
#driveBase.straight(-300) #multi
#motorFront.run_angle (1000,160) #multi 
#driveBase.straight(-310) #multi
driveBase.straight(25)
driveBase.turn(-90)
driveBase.straight(170)
driveBase.turn(-45)
#driveBase.straight(200)
#motorFront.run_angle(1000,-160)
#driveBase.straight(350)
run_task(driveAndlift(535,-160))
driveBase.turn(45)
driveBase.straight(-20)
driveBase.straight(175)
motorFront.run_angle(300,320)
driveBase.straight(-50)
motorFront.run_until_stalled(1000,Stop.COAST,65)
driveBase.turn(-45)
driveBase.straight(-155)
#print(timer.time()/1000)
driveBase.settings(straight_speed=800)
driveBase.turn(10)
driveBase.straight(-450, Stop.NONE)
driveBase.curve(-400,80)
#driveBase.turn(-30)
#driveBase.straight(-650)
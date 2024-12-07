from PortMap24 import * 
#2nd thick black line from front on edge. 
#1 square from left. facing toward corral tree
async def aaaaa():
    motorFront.run_until_stalled(100,Stop.COAST,100)
    await driveBase.straight(400)
driveBase.settings(straight_speed=150)
run_task(aaaaa())
#motorFront.run_angle(1000,10, wait=False)
#wait(100)
motorFront.run_until_stalled(-1000,Stop.COAST,30)
driveBase.settings(straight_speed=600)
driveBase.straight(-400)

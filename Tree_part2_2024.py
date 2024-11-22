from PortMap24 import * 

driveBase.settings(straight_speed=350)
motorFront.run_until_stalled(100,Stop.COAST,100)
driveBase.straight(400)
motorFront.run_until_stalled(-1000,Stop.COAST,30)
driveBase.straight(-400)

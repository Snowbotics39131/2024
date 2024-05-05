from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()
motorLeft = Motor(Port.F,Direction.CLOCKWISE)
motorRight= Motor(Port.E,Direction.COUNTERCLOCKWISE)
driveBase = DriveBase(motorRight,motorLeft,90,125)

#driveBase.straight(1575)
#driveBase.turn(90)
#driveBase.straight(100)
#driveBase.turn(135)
driveBase.straight(500)
#driveBase.turn(90)
driveBase.straight(-500)
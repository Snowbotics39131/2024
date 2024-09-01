from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import *

motorLeft = Motor(Port.E, Direction.COUNTERCLOCKWISE)
motorRight = Motor(Port.F, Direction.CLOCKWISE)
motorFront = Motor(Port.C)
motorBack = Motor(Port.A)
#colorSensorLeft = ColorSensor(Port.B)
#colorSensorRight = ColorSensor(Port.D)
driveBase = DriveBase(motorLeft,motorRight,56,114)
driveBase.use_gyro(True)

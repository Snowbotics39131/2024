from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

leftMotor = Motor(Port.C,Direction.COUNTERCLOCKWISE) 
rightMotor = Motor(Port.F,Direction.CLOCKWISE)
leftMotor.dc(1000)
rightMotor.dc(0)
wait(100000)
#driveBase = DriveBase(leftMotor,rightMotor,17.5,180)
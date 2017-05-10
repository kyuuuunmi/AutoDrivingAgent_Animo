#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
 
import time
import atexit

class MotorController:

        mh = Adafruit_MotorHAT(addr=0x60)



        def __init__(self):
                print("motor init")
                atexit.register(self.turnOffMotors)
                self.speedValue = 50
                self.myMotorL = MotorController.mh.getMotor(3)
                self.myMotorR = MotorController.mh.getMotor(4)
                self.myMotorL.setSpeed(self.speedValue)
                self.myMotorR.setSpeed(self.speedValue)

        def turnOffMotors(self):
                MotorController.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
                MotorController.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
                MotorController.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
                MotorController.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

        def driveForward(self):
                print("Forward!")
                self.myMotorL.run(Adafruit_MotorHAT.FORWARD)
                self.myMotorR.run(Adafruit_MotorHAT.FORWARD)

        def driveRight(self):
                print("Right! ")
                #for i in range(self.speedValue, 255):
                self.myMotorL.setSpeed(70)
                self.speedSetup()

        def driveLeft(self):
               print("Left! ")
               for i in range(self.speedValue, 200):
                       self.myMotorR.setSpeed(i)
                       time.sleep(0.005)
               self.speedSetup()

        def driveBackward(self):
                print("Backward! ")
                self.myMotorL.run(Adafruit_MotorHAT.BACKWARD)
                self.myMotorR.run(Adafruit_MotorHAT.BACKWARD)

        def driveRelease(self):
                print("Release")
                self.myMotorL.run(Adafruit_MotorHAT.RELEASE)
                self.myMotorR.run(Adafruit_MotorHAT.RELEASE)
                time.sleep(1.0)
                
        def speedSetup(self):
                self.myMotorL.setSpeed(self.speedValue)
                self.myMotorR.setSpeed(self.speedValue)
                
        def speedUpControl(self):
                print("\tSpeed up...")
                for i in range(self.speedValue, 100):
                        self.myMotorL.setSpeed(i)
                        self.myMotorR.setSpeed(i)
                        time.sleep(0.01)

        def speedDownControl(self):
                print("\tSlow down...")
                for i in reversed(range(self.speedValue, 100)):
                        self.myMotorL.setSpeed(i)
                        self.myMotorR.setSpeed(i)
                        time.sleep(0.01)

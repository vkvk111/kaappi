#!/bin/python

import RPi.GPIO as GPIO
from time import sleep
import math
from solenoid import launch
import sys

# 2450 steps 
# top led front 67
# bottom led front 0
# top led back 68
# bottom led back 134


class Stepper:

    def __init__(self, **kwargs):
        self.position = 0
        self.ledPosition = 0
        self.enabled = 0

        # pins
        self.DIR = kwargs.get("dir")
        self.STEP = kwargs.get("step")
        self.ENABLE = kwargs.get("enable")
        self.ZEROBTN = kwargs.get("zero")

        print(self.DIR)
        print(self.STEP)
        print(self.ENABLE)
        print(self.ZEROBTN)

        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.ENABLE, GPIO.OUT)
        GPIO.setup(self.ZEROBTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.output(self.ENABLE, GPIO.HIGH)

    def calculateLedPos(self):
        self.ledPosition = (67/2480)* self.position
        self.ledPosition = math.floor(self.ledPosition)
        return self.ledPosition

    def enableMotor(self):
        GPIO.output(self.ENABLE, GPIO.LOW)
        self.enabled = 1

    def disableMotor(self):
        GPIO.output(self.ENABLE, GPIO.HIGH)
        self.enabled = 0

    def turn(self, dir, steps, speed):

        # set direction 0 / 1
        GPIO.output(self.DIR, dir)

        if dir== 0:
            diff = -1
        else:
            diff = 1

        for i in range(steps):
            GPIO.output(self.STEP,GPIO.HIGH)
            sleep(1/(speed*2))
            GPIO.output(self.STEP,GPIO.LOW)
            sleep(1/(speed*2))

            self.position += diff

            ledPosOld = self.ledPosition
            if self.calculateLedPos() != ledPosOld:
                f = open("position.txt", "w")
                f.write(str(self.ledPosition))
                print(self.ledPosition)
                f.close()
 
        print(f"potition: {self.position}")

    def launchcan(self, solenoid=0, delay=5):
        self.disableMotor()
        launch(solenoid)
        sleep(delay)
        self.enableMotor()

    def calibrate(self):

        while (GPIO.input(self.ZEROBTN) == 1):
            self.turn(1, 1, 500)

        self.turn(1, 5, 500)

        while (GPIO.input(self.ZEROBTN) == 0):
            self.turn(0, 1, 500)

        self.position = 0


def main():
    stepper = Stepper(
        dir=23,
        step=24,
        enable=27,
        zero=26,
    )
    arg1 = sys.argv[1]
    # arg2 = sys.argv[2]

    if arg1 == "left0":
        getBotLeft(stepper)
    elif arg1 == "en":
        stepper.enableMotor()
    elif arg1 == "dis":
        stepper.disableMotor()
    elif arg1 == "cal":
        stepper.enableMotor()
        stepper.calibrate()
        stepper.disableMotor()
    elif arg1 == "up":
        stepper.enableMotor()
        speed = sys.argv[2]
        steps = sys.argv[3]
        stepper.turn(1, int(steps), int(speed))
        stepper.disableMotor()
    elif arg1 == "down":
        stepper.enableMotor()
        speed = sys.argv[2]
        steps = sys.argv[3]
        stepper.turn(0, int(steps), int(speed))
        stepper.disableMotor()
    elif arg1 == "can":
        stepper.enableMotor()
        stepper.launchcan(3, 0.1)
        stepper.disableMotor()


def getBotLeft(stepper):
    GPIO.setmode(GPIO.BCM)

    stepper.enableMotor()
    stepper.calibrate()
    stepper.turn(1, 80, 300)
    sleep(1)
    stepper.launchcan(3, 0.1)
    stepper.turn(0, 80, 300)
    sleep(2)
    stepper.turn(1, 750, 300)

    stepper.disableMotor()





main()

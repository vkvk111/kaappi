
import RPi.GPIO as GPIO
from time import sleep
import math
from solenoid import launch

# 2450 steps 
# top led front 67
# bottom led front 0
# top led back 68
# bottom led back 134

TOP_POS = 2450

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

    def launchcan(self, solenoid=0, delay=0.1):
        self.disableMotor()
        launch(solenoid)
        sleep(delay)
        self.enableMotor()

    def calibrate(self):

        while (GPIO.input(self.ZEROBTN) == 1):
            self.turn(1, 1, 500)

        self.turn(1, 5, 500)

        while (GPIO.input(self.ZEROBTN) == 0):
            self.turn(0, 1, 300)

        self.position = 0


def main():
    GPIO.setmode(GPIO.BCM)

    stepper = Stepper(
        dir=23,
        step=24,
        enable=27,
        zero=26,
    )

    stepper.enableMotor()
#    stepper.turn(1, 400, 300)
    stepper.calibrate()
    sleep(1)
    stepper.turn(1, 2450, 300)

    sleep(5)
#    stepper.launchcan(3, 0.1)

    stepper.disableMotor()


   
main()

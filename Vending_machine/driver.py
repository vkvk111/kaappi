
import RPi.GPIO as GPIO
from time import sleep
import math
from solenoid import launch

# OUTDATED INFO
# 2430 steps 
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
        f = open("position.txt", "r")
        self.position = int(f.read())

    def calculateLedPos(self):
        self.ledPosition = (67/2480) * self.position
        self.ledPosition = math.floor(self.ledPosition)
        return self.ledPosition

    def enableMotor(self):
        GPIO.output(self.ENABLE, GPIO.LOW)
        self.enabled = 1

    def disableMotor(self):
        GPIO.output(self.ENABLE, GPIO.HIGH)
        self.enabled = 0

    def turn(self, dir, steps, speed, accel=True):

        # set direction 0 / 1
        GPIO.output(self.DIR, dir)
        if accel:
            spd = 10
        else:
            spd = speed
        if dir== 0:
            diff = -1
        else:
            diff = 1

        for i in range(steps):
            GPIO.output(self.STEP,GPIO.HIGH)
            sleep(1/(spd*2))
            GPIO.output(self.STEP,GPIO.LOW)
            sleep(1/(spd*2))
            spd += 10
            if spd > speed:
                spd = speed
            self.position += diff

            f = open("position.txt", "w")
            f.write(str(self.position))
            f.close()

        #print(f"potition: {self.position}")

    def launchcan(self, solenoid=0, delay=0.1):
        self.disableMotor()
        launch(solenoid)
        sleep(delay)
        self.enableMotor()

    def calibrate(self):
        max = 2400
        while (GPIO.input(self.ZEROBTN) == 1):
            self.turn(1, 1, 500, False)
            max -= 1
            if max <= 0:
                break

        self.turn(1, 5, 500)

        while (GPIO.input(self.ZEROBTN) == 0):
            self.turn(0, 1, 500, accel=False)

        self.position = 0

        f = open("position.txt", "w")
        f.write(str(self.position))
        f.close()

    def test_button(self):
        while True:
            print(GPIO.input(self.ZEROBTN))



def main():
    GPIO.setmode(GPIO.BCM)

    stepper = Stepper(
        dir=23,
        step=24,
        enable=27,
        zero=26,
    )

    """

    stepper.enableMotor()
#    stepper.turn(1, 400, 300)
    stepper.calibrate()
    sleep(1)
    stepper.turn(1, 2450, 300)

    sleep(5)
#    stepper.launchcan(3, 0.1)

    stepper.disableMotor()
    """

    stepper.test_button()



if __name__ == "__main__":
    main()


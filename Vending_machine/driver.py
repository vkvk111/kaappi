import RPi.GPIO as GPIO
from time import sleep
#import board
#import neopixel
import math

# 2490 steps
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
#        self.LEDS = kwargs.get("leds")

        print(self.DIR)
        print(self.STEP)
        print(self.ENABLE)

        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.ENABLE, GPIO.OUT)
        GPIO.output(self.ENABLE, GPIO.HIGH)
    
#        self.ledLen = kwargs.get("led_len", 300)
#        self.leds = neopixel.NeoPixel(self.LEDS, self.ledLen)

    '''
    def enableLed(self, r, g, b):
        self.leds[self.ledPosition] = (r, g, b)

    def enableBacklight(self, r, g, b):
        for i in range(7):
            self.leds[self.ledPosition + i] = (r, g, b)
        
    def ledsOff(self):
        self.leds.fill((0, 0, 0))

    '''
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

'''
    def turnBacklight(self, dir, steps, speed, r, g, b):

        # set direction 0 / 1
        GPIO.output(self.DIR, dir)

        for i in range(steps):
            GPIO.output(self.STEP,GPIO.HIGH)
            sleep(1/(speed*2))
            GPIO.output(self.STEP,GPIO.LOW)
            sleep(1/(speed*2))

            ledPosOld = self.ledPosition
            print(self.ledPosition)
            if self.calculateLedPos(self.position + i) != ledPosOld:
                self.enableBacklight(255, 0, 0)
                print("we")
        
        if dir== 0:
            self.position -= steps
        else:
            self.position += steps

        print(f"potition: {self.position}")

'''



DIR = 16
STEP = 18
ENABLE = 13

# Set the first direction you want it to spin

def stop():
    GPIO.output(ENABLE, GPIO.HIGH)
def manual_turn():
    
    kb_in = ""
    count = 0
    while kb_in != "stop":
        kb_in = input()
        try:
            dir = int(kb_in.split()[0])
            steps = int(kb_in.split()[1])
            print(f"direction {dir}")
            print(f"{steps } steps")
            turn(dir, steps, 100)
            count += steps
            print(count)
        except:
            print("bruh")

def main():
    GPIO.setmode(GPIO.BCM)

    stepper = Stepper(
        dir=23,
        step=24,
        enable=27,
#        leds=board.D18
    )

    stepper.enableMotor()
    stepper.turn(1, 100, 300)
    sleep(5)
    stepper.turn(0, 100, 300)
    stepper.disableMotor()


#   Establish Pins in software
#    GPIO.setup(DIR, GPIO.OUT)
#    GPIO.setup(STEP, GPIO.OUT)
#    GPIO.setup(ENABLE, GPIO.OUT)

#    GPIO.output(ENABLE, GPIO.HIGH)
#    manual_turn()
#    stop()
    #pixels = neopixel.NeoPixel(board.D18, 300)

    #pixels[15] = (255, 0, 0)


   
main()

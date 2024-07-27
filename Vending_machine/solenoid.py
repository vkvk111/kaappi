import RPi.GPIO as GPIO
from time import sleep
#import board
import math

#
#
#
# 19 = ala vasen

pins = [5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)

def launch(n):

    GPIO.setup(pins[n], GPIO.OUT)
    GPIO.output(pins[n], GPIO.HIGH)

    sleep(0.5)

    GPIO.output(pins[n], GPIO.LOW)

if __name__ == "__main__":
    print("LAUNCHING SOLENOID")
#    launch(0)
#    launch(1)
#    launch(2)
    launch(3)

import RPi.GPIO as GPIO
from time import sleep
#import board
import math

pins = [5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)

for i in pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

input()
for i in pins:
    GPIO.output(i, GPIO.LOW)

GPIO.cleanup()

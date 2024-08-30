import RPi.GPIO as GPIO
from time import sleep
import board
import neopixel
import math

pixels = neopixel.NeoPixel(board.D18, 300)

def main():


    f = open("position.txt", "r")
    pos_old = 0

    same_count = 0
    while True:


        f = open("position.txt", "r")
        try:
            pos = int(int(f.read()) * 67/2480)
                
            pos_old = pos

            led_amount = 6

            pixels[0:300] = [(0,0,0) for i in range (300)]
            pixels[pos: pos+led_amount] = [(255,0,0) for i in range(led_amount)]

        except:
            pos = 0

        f.close()

main()
    

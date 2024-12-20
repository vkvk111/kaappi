import RPi.GPIO as GPIO
from time import sleep
import board
import neopixel
import math

pixels = neopixel.NeoPixel(board.D18, 300)

def main():

    led_amount = 6

    f = open("position.txt", "r")

    pos_old = 0
    same_count = 0
    while True:


        f = open("position.txt", "r")
        try:
            pos = int(int(f.read()) * 58/2430) + 9
            pos2 = 144 - pos
                

            if pos != pos_old:
                pixels[0:300] = [(0,0,0) for i in range (300)]
                pixels[pos: pos+led_amount] = [(255,0,0) for i in range(led_amount)]
                pixels[pos2-led_amount: pos2] = [(255,0,0) for i in range(led_amount)]

            pos_old = pos

        except:
            pos = 0

        f.close()

main()
#pixels.fill((255,0,0))

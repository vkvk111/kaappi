#!/bin/python3

import RPi.GPIO as GPIO
from time import sleep
import board
import neopixel
import math


pixels = neopixel.NeoPixel(board.D18, 300)

color = (255,255,255)

def load_color():
    try:
        f = open("color.txt", "r")
        clr = f.read().split(",")
        r = int(clr[0])
        g = int(clr[1])
        b = int(clr[2])
        f.close()
    except:
        r = 0
        g = 0
        b = 0

    return ((r,g,b))



def main():

    led_amount = 6

    f = open("position.txt", "r")

    pos_old = 0
    same_count = 0
    while True:

        color = load_color()

        f = open("position.txt", "r")
        try:
            pos = int(int(f.read()) * 58/2430) + 9
            pos2 = 144 - pos
                

            if pos != pos_old:
                pixels[0:300] = [(0,0,0) for i in range (300)]
                pixels[pos: pos+led_amount] = [color for i in range(led_amount)]
                pixels[pos2-led_amount: pos2] = [color for i in range(led_amount)]

            pos_old = pos

        except:
            pos = 0

        f.close()

main()
#pixels.fill(color)
#pixels[85:135] = [color for i in range (300)]


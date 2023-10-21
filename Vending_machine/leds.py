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
        pos = int(f.read())

        if  pos == pos_old:
            same_count += 1
            print(same_count)
            if same_count >= 10:
                same_count = 0

                for i in range(300):
                    pixels[299-i] = (0,0,0)
            
        pos_old = pos

        led_amount=16

        for i in range(led_amount):
            pixels[pos + i] = (255, 0, 0)

        pixels[pos + led_amount] = (0, 0, 0)
        pixels[pos + led_amount + 1] = (0, 0, 0)
        if pos > 2:
            pixels[pos - 2] = (0, 0, 0)
            pixels[pos - 3] = (0, 0, 0)
        


        f.close()







try:   
    main()
except:
    pixels.fill((0,0,0))
    

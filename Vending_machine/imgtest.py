from PIL import Image
import os
import numpy
from time import sleep

def filter_greyscale(img):
    new_img = []

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r = img.getpixel((x,y))[0]
            g = img.getpixel((x,y))[1]
            b = img.getpixel((x,y))[2]

            if abs(r - g) > 50 or abs(g - b) > 50 or abs(r - b) > 50:
                new_img.append([r,g,b])
            
    #print(numpy.array(new_img))
    #return Image.fromarray(numpy.array(new_img))
    return new_img


def get_color():
    os.system("fswebcam --no-banner image.jpg")
    img = Image.open("image.jpg")

    r = 0; g = 0; b = 0
    imgsize = img.size[0] * img.size[1]

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r += img.getpixel((x,y))[0]
            g += img.getpixel((x,y))[1]
            b += img.getpixel((x,y))[2]

    return (int(r/imgsize), int(g/imgsize), int(b/imgsize))


def get_color2():
    os.system("fswebcam --no-banner image.jpg")
    img = Image.open("image.jpg")

    img = filter_greyscale(img)
    print(img)

    r_p = img.histogram()[0:256]
    g_p = img.histogram()[257:512]
    b_p = img.histogram()[513:768]

    r = r_p.index(max(r_p))
    g = g_p.index(max(g_p))
    b = b_p.index(max(b_p))
    
    return(r,g,b)


def get_color3():
    os.system("fswebcam --no-banner image.jpg")
    img = Image.open("image.jpg")

    img = filter_greyscale(img)
    imgsize = len(img)

    r = sum([i[0] for i in img])
    g = sum([i[1] for i in img])
    b = sum([i[2] for i in img])

    return (int(r/imgsize), int(g/imgsize), int(b/imgsize))


def postprocess(color):
    new_col = [0,0,0]

    for i in range(len(new_col)):
        if color[i] < 40:
            new_col[i] = int(color[i] / 10)
        if color[i] < 80:
            new_col[i] = int(color[i] / 5)
        if color[i] < 120:
            new_col[i] = int(color[i] / 3)
        else:
            new_col[i] = color[i]

    return tuple(new_col)


def get_data(auto=True, delay=5):
    t = "stronkelo" 
    n = 1

    while True:
        if not auto:
            print("<Return> to take pic")
            input()

        os.system(f"fswebcam --no-banner training_data/img_{t}_{n}.jpg")
        print(f"Image saved in training_data/img_{t}_{n}.jpg")
        sleep(delay)        
        n += 1



if __name__ == "__main__":
    """
    color = get_color3()
    color = postprocess(color)
    print(color)

    f = open("color.txt", "w")
    f.write(f"{color[0]},{color[1]},{color[2]}")
    f.close()
    """

    get_data(auto=False,delay=0)

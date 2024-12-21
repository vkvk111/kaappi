from PIL import Image

def get_color():
    img = Image.open("image.jpg")
    r = 0; g = 0; b = 0
    imgsize = img.size[0] * img.size[1]

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r += img.getpixel((x,y))[0]
            g += img.getpixel((x,y))[1]
            b += img.getpixel((x,y))[2]

    return (int(r/imgsize), int(g/imgsize), int(b/imgsize))

if __name__ == "__main__":
    print(get_color(img))


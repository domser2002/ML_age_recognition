import cv2
from PIL import Image, ImageDraw
from numpy import asarray
import numpy
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def average_pixel_color_and_brightness(path):
    def brightness(R,G,B):
        return 0.2126*R + 0.7152*G + 0.0722*B
    files=os.listdir(path)
    n=len(files)
    average_red=[0]*n
    average_green=[0]*n
    average_blue=[0]*n
    average_brightness=[0]*n
    i=0
    for file in files:
        image=cv2.imread((os.path.join(path,file)))
        average_color_row = numpy.average(image, axis=0)
        average_color = numpy.average(average_color_row, axis=0)
        r=average_color[0]
        g=average_color[1]
        b=average_color[2]
        average_red[i]=r
        average_green[i]=g
        average_blue[i]=b
        average_brightness[i]=brightness(r,g,b)
        i=i+1
    red=numpy.average(average_red)
    green=numpy.average(average_green)
    blue=numpy.average(average_blue)
    brightness=numpy.average(average_brightness)
    return [[red,green,blue],brightness]

def draw_average_color_graph(colors,filename,width,height):
    n=len(colors)
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    for i in range(n - 1):
        color1 = colors[i]
        color2 = colors[i + 1]
        if not isinstance(color1,list) or len(color1)!=3 or not isinstance(color2,list) or len(color2)!=3:
            print(color1)
            print(color2)
            print("Not a color!")
            return
        x_start = int((width / len(colors)) * i)
        x_end = int((width / len(colors)) * (i + 1))
        color1=(int(color1[0]),int(color1[1]),int(color1[2]))
        color2=(int(color2[0]),int(color2[1]),int(color2[2]))
        draw.rectangle([(x_start, 0), (x_end, height)], fill=color1)
        draw.rectangle([(x_end, 0), (x_end + 1, height)], fill=color2)
    if not os.path.exists(filename):
        open(filename,'w')
    image.save(filename)
    return

import cv2
from PIL import Image
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

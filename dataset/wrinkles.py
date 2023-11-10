import cv2
from PIL import Image
from numpy import asarray
import numpy


# calculates the average amount of edges in "files"
def wrinkles(files):
    n = len(files)
    arr = [0]*n
    for i in range(0, n):
        temp = cv2.cvtColor(asarray(Image.open(files[i])), cv2.COLOR_BGR2GRAY)
        arr[0] = numpy.average(cv2.Canny(cv2.GaussianBlur(src=temp, ksize=(3, 5), sigmaX=0.5), 70, 135))
    return numpy.average(arr)

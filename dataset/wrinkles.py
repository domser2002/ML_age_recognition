import cv2
from PIL import Image
from numpy import asarray
import numpy
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# calculates what % of image is covered by edges on average in files located in "path"
def wrinkles(path):
    n = len(os.listdir(path))
    arr = [0] * n
    i = 0
    for file in os.listdir(path):
        temp = cv2.cvtColor(asarray(Image.open(os.path.join(path, file))), cv2.COLOR_BGR2GRAY)
        arr[i] = numpy.average(cv2.Canny(cv2.GaussianBlur(src=temp, ksize=(3, 5), sigmaX=0.5), 70, 135))
        i += 1
    return numpy.average(arr) * 100 / 255


# draws histogram of average edge percentages from vector "data"
def wrinkles_histogram(data):
    fig, ax = plt.subplots()
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.bar(numpy.array(list(range(1, len(data) + 1))), numpy.array(data))
    plt.ylim(0, 100)
    plt.title('Średnia gęstość krawędzi na zdjęciach z poszczególnych grup wiekowych')
    plt.xlabel('Wiek')
    plt.ylabel('Procent pokrycia obrazu przez krawędzie')
    plt.savefig('rozklad_krawedzie.jpg')

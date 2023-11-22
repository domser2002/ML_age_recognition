import numpy
import os
from PIL import Image
from contrast import contrast as c
from blackness import blackness as b
# wrappers for functions that take numpy.array as an argument


def contrast(path):
    if os.path.isdir(path):
        n = len(os.listdir(path))
        arr = [0] * n
        i = 0
        for file in os.listdir(path):
            arr[i] = c(numpy.asarray(Image.open(os.path.join(path, file))))
            i += 1
        return numpy.average(arr)
    return c(numpy.asarray(Image.open(path)))


def blackness(path):
    if os.path.isdir(path):
        n = len(os.listdir(path))
        arr = [0] * n
        i = 0
        for file in os.listdir(path):
            arr[i] = b(numpy.asarray(Image.open(os.path.join(path, file))))
            i += 1
        return numpy.average(arr)
    return b(numpy.asarray(Image.open(path)))
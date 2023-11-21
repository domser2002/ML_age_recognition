import cv2
import numpy as np

def contrast(img : np.array):
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_contrast = img_grey.std()
    return img_contrast
import cv2
import numpy as np

def blackness(img : np.array):
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(img_grey, 128, 255, 0)
    number_of_white_pix = np.sum(binary == 255)
    number_of_black_pix = np.sum(binary == 0)
    number_of_pix = number_of_white_pix + number_of_black_pix
    image_blackness = number_of_black_pix * 100 / number_of_pix
    return image_blackness
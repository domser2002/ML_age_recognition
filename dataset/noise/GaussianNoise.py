import cv2
import numpy as np
import os

def gaussian_noise(path,output_path, mean=0, stddev=180):
    img = cv2.imread(path)
    if img is None:
        print(f"Error: Unable to load the image at {path}")
        return
    noise = np.zeros(img.shape, np.uint8)
    cv2.randn(noise, mean, stddev)
    noisy_img = cv2.add(img, noise)
    cv2.imwrite(output_path, noisy_img)

gaussian_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Gaussian.jpg")

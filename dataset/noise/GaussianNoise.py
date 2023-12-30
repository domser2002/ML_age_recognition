import cv2
import numpy as np

def gaussian_noise(path,output_path, mean=0, stddev=180):
    img = cv2.imread(path)
    if img is None:
        print(f"Error: Unable to load the image at {path}")
        return
    noise = np.zeros(img.shape, np.uint8)
    cv2.randn(noise, mean, stddev)
    noisy_img = cv2.add(img, noise)
    cv2.imwrite(output_path, noisy_img)

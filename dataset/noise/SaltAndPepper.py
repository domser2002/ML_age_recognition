import cv2
import numpy as np

def salt_and_pepper_noise(path,output_path, amount=0.05):
    img = cv2.imread(path)
    if img is None:
        print(f"Error: Unable to load the image at {path}")
        return
    salt_and_pepper = np.random.rand(*img.shape[:2])
    salt = salt_and_pepper < amount / 2.0
    pepper = salt_and_pepper > 1 - amount / 2.0
    img[salt] = 255
    img[pepper] = 0
    cv2.imwrite(output_path, img)
import cv2
import numpy as np

def speckle_noise(path,output_path, variance=0.02):
    img = cv2.imread(path)
    if img is None:
        print(f"Error: Unable to load the image at {path}")
        return
    noise = np.random.normal(0, variance, img.shape)
    noisy_img = img + img * noise
    cv2.imwrite(output_path, noisy_img)
    print(f"Noisy image saved at: {output_path}")
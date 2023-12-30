import cv2
import numpy as np

def poisson_noise(path,output_path):
    img = cv2.imread(path)
    if img is None:
        print(f"Error: Unable to load the image at {path}")
        return
    noisy_img = np.random.poisson(img.astype(np.float64) / 255.0) * 255.0
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
    cv2.imwrite(output_path, noisy_img)

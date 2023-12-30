import cv2
import numpy as np

def quantization_noise(path, output_path, levels=16):
    img = cv2.imread(path)
    if img is None:
        print(f"Error: Unable to load the image at {path}")
        return
    quantization_levels = 256 // levels
    noisy_img = (img / quantization_levels) * quantization_levels
    cv2.imwrite(output_path, noisy_img)
    
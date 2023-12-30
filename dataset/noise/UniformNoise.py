import cv2
import numpy as np

def uniform_noise(path, output_path, low=0, high=50):
    img = cv2.imread(path)
    if img is None:
        print(f"Error: Unable to load the image at {path}")
        return
    noise = np.random.uniform(low, high, img.shape).astype(np.uint8)
    noisy_img = cv2.add(img, noise)
    cv2.imwrite(output_path, noisy_img)
    print(f"Noisy image saved at: {output_path}")


from PIL import Image, ImageEnhance
import random

def adjust_brightness(input_path, output_path):
    # Open the image file
    original_image = Image.open(input_path)

    # Generate a random brightness factor between 0.5 and 1.5
    brightness_factor = random.uniform(1.2, 1.5)

    # Create an enhancer object and apply the brightness factor
    enhancer = ImageEnhance.Brightness(original_image)
    brightened_image = enhancer.enhance(brightness_factor)

    # Save the brightened or darkened image
    brightened_image.save(output_path)

if __name__ == "__main__":
    # Specify the input image path and the output image path
    input_image_path = "input_image.png"  # Change to your input image path
    output_image_path = "brightened_image.png"  # Change to your desired output image path

    # Call the function to adjust brightness and save the image
    adjust_brightness(input_image_path, output_image_path)
from PIL import Image
import random
import math

def rotate_image(input_path, output_path):
    # Open the image file
    original_image = Image.open(input_path)

    # Generate a random rotation angle between 30 and 90 degrees
    rotation_angle = random.uniform(30, 90)

    # Rotate the image
    rotated_image = original_image.rotate(rotation_angle,expand=True)

    # Get the size of the rotated image
    width, height = rotated_image.size

    # Create a copy of the rotated image to modify
    colorized_image = rotated_image.copy()

    # Iterate over each pixel
    for x in range(width):
        for y in range(height):
            # Get the pixel color at the current position
            pixel_color = rotated_image.getpixel((x, y))

            # Check if the pixel color is black
            if pixel_color == (0, 0, 0):
                # Replace black pixel with a random color
                random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                colorized_image.putpixel((x, y), random_color)

    # Save the colorized image
    colorized_image.save(output_path)

if __name__ == "__main__":
    input_image_path = "input_image.png" 
    output_image_path = "left_rotated_image.png"

    rotate_image(input_image_path, output_image_path)
from PIL import Image,ImageFilter

def simple_blur(path,output_path):
    img = Image.open(path)
    blurimg=img.filter(ImageFilter.BLUR)
    blurimg.save(output_path)
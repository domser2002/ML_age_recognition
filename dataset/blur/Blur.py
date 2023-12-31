from PIL import Image,ImageFilter
import os

def blur(path,output_path,blur):
    img = Image.open(path)
    blurimg=img.filter(blur)
    blurimg.save(output_path)

def blur_image(path):
    blur(path,os.path.join(os.path.dirname(path), "simple_blur_" + os.path.basename(path)),ImageFilter.BLUR)
    blur(path,os.path.join(os.path.dirname(path), "box_blur_" + os.path.basename(path)),ImageFilter.BoxBlur(5))
    blur(path,os.path.join(os.path.dirname(path), "gaussian_blur_" + os.path.basename(path)),ImageFilter.GaussianBlur(5))
    blur(path,os.path.join(os.path.dirname(path), "unsharp_mask_" + os.path.basename(path)),ImageFilter.UnsharpMask(2,150,3))
    blur(path,os.path.join(os.path.dirname(path), "median_blur_" + os.path.basename(path)),ImageFilter.MedianFilter(5))

def blur_dirctory(path):
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            blur_image(full_path)

#demo
blur('/home/domser/studia/semestr5/ML/dlib/repo/dataset/blur/test.jpg',
     '/home/domser/studia/semestr5/ML/dlib/repo/dataset/blur/simple.jpg',
     ImageFilter.BLUR)
blur('/home/domser/studia/semestr5/ML/dlib/repo/dataset/blur/test.jpg',
     '/home/domser/studia/semestr5/ML/dlib/repo/dataset/blur/box.jpg',
     ImageFilter.BoxBlur(5))
blur('/home/domser/studia/semestr5/ML/dlib/repo/dataset/blur/test.jpg',
     '/home/domser/studia/semestr5/ML/dlib/repo/dataset/blur/gaussian.jpg',
     ImageFilter.GaussianBlur(5))
blur('/home/domser/studia/semestr5/ML/dlib/repo/dataset/blur/test.jpg',
     '/home/domser/studia/semestr5/ML/dlib/repo/dataset/blur/unsharp.jpg',
     ImageFilter.UnsharpMask(2,150,3))
blur('/home/domser/studia/semestr5/ML/dlib/repo/dataset/blur/test.jpg',
     '/home/domser/studia/semestr5/ML/dlib/repo/dataset/blur/median.jpg',
     ImageFilter.MedianFilter(5))
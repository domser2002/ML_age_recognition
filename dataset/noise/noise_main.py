from GaussianNoise import *
from SaltAndPepper import *
from PoissonNoise import *
from SpeckleNoise import *
from UniformNoise import *
from QuantizationNoise import *
import os

def noise_image(path):
    gaussian_noise(path,os.path.join(os.path.dirname(path),'gaussian_noise_'+os.path.basename(path)))
    salt_and_pepper_noise(path,os.path.join(os.path.dirname(path),'salt_and_pepper_noise_'+os.path.basename(path)))
    poisson_noise(path,os.path.join(os.path.dirname(path),'poisson_noise_'+os.path.basename(path)))
    uniform_noise(path,os.path.join(os.path.dirname(path),'uniform_noise_'+os.path.basename(path)))
    quantization_noise(path,os.path.join(os.path.dirname(path),'quantization_noise_'+os.path.basename(path)))

def noise_directory(path):
    for filename in os.listdir(path):
        fullpath=os.path.join(path,filename)
        if os.path.isfile(fullpath):
            noise_image(fullpath)

#demo
gaussian_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Gaussian.jpg")
salt_and_pepper_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/SaltAndPepper.jpg")
poisson_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Poisson.jpg")
speckle_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Speckle.jpg")
uniform_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Uniform.jpg")
quantization_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Quantization.jpg")
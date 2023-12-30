from GaussianNoise import *
from SaltAndPepper import *
from PoissonNoise import *
from SpeckleNoise import *
from UniformNoise import *
from QuantizationNoise import *

gaussian_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Gaussian.jpg")
salt_and_pepper_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/SaltAndPepper.jpg")
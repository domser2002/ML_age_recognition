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
poisson_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Poisson.jpg")
speckle_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Speckle.jpg")
uniform_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Uniform.jpg")
quantization_noise("/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/test.jpg",
               "/home/domser/studia/semestr5/ML/dlib/repo/dataset/noise/Quantization.jpg")
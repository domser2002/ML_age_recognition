import os
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
from torch.utils.data import Dataset, DataLoader, random_split
import cv2
from PIL import Image
from torchvision import datasets, models
from torchvision.models import ResNet50_Weights

class AgeDetector:
    def __init__(self, path_to_weights):
        self.image_size=224
        self.transform = transforms.Compose([
            transforms.Resize((self.image_size, self.image_size)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.4914, 0.4822, 0.4465],
                std=[0.2023, 0.1994, 0.2010],)
        ])
        self.device = torch.device("cpu")
        self.model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V2).to(self.device)

        for param in self.model.parameters():
            param.requires_grad = False
        self.model.fc = nn.Sequential(
            nn.Linear(2048, 512),
            nn.ReLU(inplace=True),
            
            nn.Linear(512, 512),
            nn.ReLU(inplace=True),
            
            nn.Linear(512, 512),
            nn.ReLU(inplace=True),
            
            nn.Linear(512, 1)
        ).to(self.device)
        self.model = torch.load(path_to_weights, map_location=self.device)

    def detect_age(self, test_img):
        test_img = Image.fromarray(test_img, mode='RGB')
        test_img = self.transform(test_img).to(self.device).detach().reshape((1, 3, self.image_size, self.image_size))
        age = float(self.model(test_img))
        age = round(age)
        return age

    def test_detector(self, img_path):
        print(self.detect_age(cv2.imread(img_path)))

detector = AgeDetector('/home/domser/studia/semestr5/ML/dlib/repo/age_detection/age_models/resnet_5.pt')
detector.test_detector('/home/domser/studia/semestr5/ML/dlib/repo/age_detection/lenna.png')

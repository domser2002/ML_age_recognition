import os
import onnx
import numpy as np
from PIL import Image
import onnxruntime as rt
from torchvision import transforms

class AgeDetector:

    def __init__(self, onnx_path = None):
        if onnx_path is None:
            onnx_path = os.path.join('age_detection', 'age_models', 'inception3.onnx')

        self.sess = rt.InferenceSession(onnx_path, providers=rt.get_available_providers())
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])
        self.input_name = self.sess.get_inputs()[0].name
        self.output_name = self.sess.get_outputs()[0].name

    def detect_age(self, img: np.array):
        PIL_img = Image.fromarray(img, mode='RGB')
        img_transform = self.transform(PIL_img).numpy().reshape((1, 3, 224, 224))
        res = self.sess.run([self.output_name], {self.input_name: img_transform})
        res = res[0][0][0]
        return res
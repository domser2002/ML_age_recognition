import os
import torch
import numpy as np
import pandas as pd
import cv2

class Detector:
	
	def __init__(self):
		# load models/best_1.pt model
		self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=os.path.join('models', 'best_1.pt'), force_reload=True)
	
	# returns bounding boxes of faces in an img
	def predict(self, img):
		return np.array(self.model(img).pandas().xyxy[0])
	
	# returns img with drawn boxes
	@staticmethod
	def draw_bounding_boxes(img, boxes):
		res = img
		for i in range(boxes.shape[0]):
			print(i)
			x, y, w, h = boxes[i][0], boxes[i][1], boxes[i][2], boxes[i][3]
			x, y, w, h = int(x), int(y), int(w), int(h)
			res = cv2.rectangle(res, (x, y), (w, h), color=(255, 0, 0))
		return res

# function showing usage of Detector class
def example():
	
	# load image
	img = cv2.imread('workers.jpg')
	
	# resize image
	img = cv2.resize(img, (int(img.shape[0] / 3), 500))
	
	# make new detector
	detector = Detector()
	
	# get bounding boxes
	boxes = detector.predict(img)
	
	# apply boxes to image
	img_boxes = Detector.draw_bounding_boxes(img, boxes)
	
	# show image
	cv2.imshow('workers', img_boxes)
	cv2.waitKey(0)

if __name__ == '__main__':
	example()

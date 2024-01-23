import sys
import os
sys.path.append(os.path.abspath('.'))
import fnmatch
from age_detection import AgeDetector
from face_detection.face_detection import Detector
import cv2

print("********TEST AGE DETECTION ON DIRECTORY**********")
print("Requirments:")
print("- directory must contain jpg images")
print("- for each image txt file with correct result must be provided")
print("- naming convension must be like in documentation")
path = "../../case_studies/directory"
print(f"Default path is {path}")
finished = False
leave = False
while finished == False:
    print("Leave default path?[y/n]")
    x = input()
    finished = True
    if x=="y":
        leave = True
    elif x=="n":
        leave = False
    else:
        finished=False
if leave == False:
    print("Enter a directory path (relative or absolute):")
    path = input()
    correct = False
    while correct == False:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        if not os.path.exists(path):
            print("Path does not exist!")
            print("Input correct path:")
            path = input()
        elif not os.path.isdir(path):
            print("Path is not a directory!")
            print("Input path to a directory:")
            path = input()
        else:
            correct = True
count = len(fnmatch.filter(os.listdir(path), '*.jpg*'))
print(f"Read {count} jpg files")
face_detector = Detector(os.path.join("face_detection","models","best_nano_1.onnx"))
age_detector = AgeDetector()
face_count = 0
error = 0
try:
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.lower().endswith('.jpg'):
                txtfile = os.path.join(path,os.path.basename(entry.name).rsplit('.', 1)[0] + '_correct.txt')
                print(txtfile)
                with open(txtfile, 'r') as file:
                    ages_correct = [int(line.strip()) for line in file]
                img = cv2.imread(entry.path)
                faces = face_detector.predict(img)
                ages_prediction = []
                for face in faces:
                    x, y = face[0], face[1]
                    x2,y2 = face[2], face[3]
                    x, y = int(x), int(y)
                    x2,y2=int(x2),int(y2)
                    cut_face = img[x:x2,y:y2]
                    prediction = age_detector.detect_age(cut_face)
                    ages_prediction.append(prediction)
                ages_correct.sort()
                ages_prediction.sort()
                for i in range(0,len(ages_correct)):
                    error = error + abs(ages_correct[i]-ages_prediction[i])
                    face_count = face_count + 1
    average_error = error / face_count
    print(f"Average error on this directory is {average_error}")
except PermissionError:
    print(f"Permission error accessing directory: {path}")

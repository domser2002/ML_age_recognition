from age_detection import AgeDetector
from face_detection.face_detection import Detector
from recognition import FaceRecognizer
import os
import json
import cv2
import numpy as np

class DataReader:
    def __init__(self,option):
        self.age_detector=AgeDetector(os.path.join('age_detection','age_models','resnet_5.pt'))
        match option:
            case '1':
                self.read_directory()
            case '2':
                self.read_video()
            case '3':
                self.read_camera()
        return
    def read_directory(self):
        print("reading from directory")

        # Get the current working directory (default = ML_age_recognition Folder)
        current_directory = os.getcwd()

        # Get target directory
        print("Possible options:")
        print("1. Read data from Current Working Directory:", current_directory)
        print("2. Read data from an Absolute Path")
        option=input()
        match option:
            case '1':
                target = current_directory
            case '2':
                target = input()
            
        extension1 = ".png"
        extension2 = ".jpg"

        path = os.path.join('face_detection', 'models', 'best_nano_1.onnx')
        # make new detector
        detector = Detector(path)

        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        # fontScale
        scale = 1
        # Blue color in BGR
        color = (0, 255, 0)
        # Line thickness of 2 px
        thickness = 2

        # Create a metadata array and fill it with important data
        metadata = {}
        targets = os.listdir(target)
        for filename in targets:
            if filename.endswith(extension1) or filename.endswith(extension2):
                img = cv2.imread(os.path.join(target, filename))
                # get bounding boxes
                boxes = detector.predict(img)
                # apply boxes to image
                img_boxes = Detector.draw_bounding_boxes(img, boxes)
                for i in range(boxes.shape[0]):
                    x, y = boxes[i][0], boxes[i][1]
                    x2,y2 = boxes[i][2], boxes[i][3]
                    x, y = int(x), int(y)
                    x2,y2=int(x2),int(y2)
                    coords = (x, y)
                    face = img[x:x2,y:y2]
                    img_boxes = cv2.putText(img_boxes, 'Age: '+str(self.age_detector.detect_age(face)), coords, font, scale, color, thickness, cv2.LINE_AA)
                cv2.imwrite(os.path.join(target, f'boxes_{filename}'), img_boxes)

        return
    

    def read_video(self):
        print("reading from video")

        print("Input video file path:")
        path = input()
        print("Output video file path (video file in .mp4 format)")
        output_path = input()

        # get video and information about input video
        vid = cv2.VideoCapture(path)
        fps = vid.get(cv2.CAP_PROP_FPS)
        ret, frame = vid.read()
        height, width, layers = frame.shape

        # create output video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output_video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        path = os.path.join('face_detection', 'models', 'best_nano_1.onnx')
        # make new detector
        detector = Detector(path)

        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        # fontScale
        scale = 1
        # Blue color in BGR
        color = (0, 255, 0)
        # Line thickness of 2 px
        thickness = 2

        while (True):
            ret, frame = vid.read()
            if ret:
                # get bounding boxes
                boxes = detector.predict(frame)
                # apply boxes to image
                img_boxes = Detector.draw_bounding_boxes(frame, boxes)
                for i in range(boxes.shape[0]):
                    x, y = boxes[i][0], boxes[i][1]
                    x2,y2 = boxes[i][2], boxes[i][3]
                    x, y = int(x), int(y)
                    x2, y2 = int(x2), int(y2)
                    coords = (x, y)
                    face=frame[x:x2,y:y2]
                    img_boxes = cv2.putText(img_boxes, 'Age: '+str(self.age_detector.detect_age(face)), coords, font, scale, color, thickness, cv2.LINE_AA)
                # write img_boxes image to output video
                output_video.write(img_boxes)
            else:
                break

        output_video.release()
        vid.release()
        cv2.destroyAllWindows()
        return
    def read_camera(self):
        print("reading from camera")

        vid = cv2.VideoCapture(0)

        path = os.path.join('face_detection', 'models', 'best_nano_1.onnx')
        # make new detector
        detector = Detector(path)

        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        # fontScale
        scale = 1
        # Blue color in BGR
        color = (0, 255, 0)
        # Line thickness of 2 px
        thickness = 2

        while (True):
            # Capture the video frame
            # by frame
            ret, frame = vid.read()

            # get bounding boxes
            boxes = detector.predict(frame)

            # apply boxes to image
            img_boxes = Detector.draw_bounding_boxes(frame, boxes)
            for i in range(boxes.shape[0]):
                x, y = boxes[i][0], boxes[i][1]
                x2,y2 = boxes[i][2], boxes[i][3]
                x, y = int(x), int(y)
                x2, y2 = int(x2), int(y2)
                coords = (x, y)
                face = frame[x:x2,y:y2]
                img_boxes = cv2.putText(img_boxes, 'Age: ' + str(self.age_detector.detect_age(face)), coords, font, scale, color,
                                        thickness, cv2.LINE_AA)

            # Display the resulting frame
            cv2.imshow('frame', img_boxes)
            
            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return
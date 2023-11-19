from age_detection import AgeDetector
from face_detection.face_detection import Detector
from recognition import FaceRecognizer
import os
import json
import cv2

class DataReader:
    def __init__(self,option):
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

        # Create a metadata array and fill it with important data
        metadata = {}
        for filename in os.listdir(target):
            if filename.endswith(extension1) or filename.endswith(extension2):
                metadata[filename] = {
                    "label": 0,  # Modify this as needed
                    # Add any more relevant data to save to the json file
                }

        # Save metadata array as a json file
        with open("pictures_metadata.json", 'w') as metadata_file:
                json.dump(metadata, metadata_file, indent=4)

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

        while (True):
            ret, frame = vid.read()
            if ret:
                # get bounding boxes
                boxes = detector.predict(frame)

                # apply boxes to image
                img_boxes = Detector.draw_bounding_boxes(frame, boxes)

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

        while (True):
            # Capture the video frame
            # by frame
            ret, frame = vid.read()

            # get bounding boxes
            boxes = detector.predict(frame)

            # apply boxes to image
            img_boxes = Detector.draw_bounding_boxes(frame, boxes)

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
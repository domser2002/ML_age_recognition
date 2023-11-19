from age_detection import AgeDetector
from recognition import FaceRecognizer
import os
import json

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
        return
    def read_camera(self):
        print("reading from camera")
        return
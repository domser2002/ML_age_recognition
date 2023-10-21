from recognition import FaceRecongnizer
from read_data import DataReader

print("Possible options:")
print("1. Read data from directory")
print("2. Read data from video")
print("3. Read data from built-in camera")
print("Choose option number:")
option=input()
dr=DataReader(option)

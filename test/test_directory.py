import os

print("********TEST AGE DETECTION ON DIRECTORY**********")
print("Requirments:")
print("- directory must contain jpg images")
print("- for each image txt file with correct result must be provided")
print("- naming convension must be like in documentation")
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
print(path)
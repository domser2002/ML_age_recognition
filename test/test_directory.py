import os
import fnmatch

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
try:
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.lower().endswith('.jpg'):
                txtfile = os.path.basename(entry.name).rsplit('.', 1)[0] + '_correct.txt'
                print(txtfile)
except PermissionError:
    print(f"Permission error accessing directory: {path}")

import os

print("********TEST AGE DETECTION ON DIRECTORY**********")
print("Requirments:")
print("- directory must contain jpg images")
print("- for each image txt file with correct result must be provided")
print("- naming convension must be like in documentation")
print("Enter a directory path (relative or absolute):")
path = input()

if os.path.isabs(path):
    print("Absolute path provided.")
else:
    path = os.path.abspath(path)
    print(f"Converted relative path to absolute path: {path}")

print(path)
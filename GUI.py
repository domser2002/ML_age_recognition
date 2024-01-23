import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkVideoPlayer import TkinterVideo
from PIL import Image, ImageTk
from numpy import asarray
import cv2
import os
from age_detection import AgeDetector
from face_detection.face_detection import Detector


def select_directory():
    global images_array
    global iterator
    target = fd.askdirectory()

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
                x, y = int(x), int(y)
                x2, y2 = boxes[i][2], boxes[i][3]
                x2, y2 = int(x2), int(y2)
                face=img[y:y2,x:x2]
                coords = (x, y)
                img_boxes = cv2.putText(img_boxes, 'Age: ' + str(age_detector.detect_age(face)), coords, font, scale, color,
                                        thickness, cv2.LINE_AA)
            cv2.imwrite(os.path.join(target, f'boxes_{filename}'), img_boxes)
            images_array.append(img_boxes)
    if len(images_array) != 0:
        size = 700, 500
        img = images_array[0]
        img = Image.fromarray(img)
        img.thumbnail(size, Image.Resampling.LANCZOS)
        numpy_img_array = asarray(img)
        opencv_image = cv2.cvtColor(numpy_img_array, cv2.COLOR_BGR2RGBA)
        # Capture the latest frame and transform to image
        captured_image = Image.fromarray(opencv_image)
        # Convert captured image to photoimage
        photo_image = ImageTk.PhotoImage(image=captured_image)
        label.photo_image = photo_image
        label.configure(image=photo_image)
        iterator = 0

def next_image():
    global images_array
    global iterator
    iterator += 1
    if iterator >= len(images_array):
        iterator = 0
    if len(images_array) != 0:
        size = 700, 500
        img = images_array[iterator]
        img = Image.fromarray(img)
        img.thumbnail(size, Image.Resampling.LANCZOS)
        numpy_img_array = asarray(img)
        opencv_image = cv2.cvtColor(numpy_img_array, cv2.COLOR_BGR2RGBA)
        # Capture the latest frame and transform to image
        captured_image = Image.fromarray(opencv_image)
        # Convert captured image to photoimage
        photo_image = ImageTk.PhotoImage(image=captured_image)
        label.photo_image = photo_image
        label.configure(image=photo_image)

def previous_image():
    global images_array
    global iterator
    iterator -= 1
    if iterator < 0:
        iterator = len(images_array)
    if len(images_array) != 0:
        size = 700, 500
        img = images_array[iterator]
        img = Image.fromarray(img)
        img.thumbnail(size, Image.Resampling.LANCZOS)
        numpy_img_array = asarray(img)
        opencv_image = cv2.cvtColor(numpy_img_array, cv2.COLOR_BGR2RGBA)
        # Capture the latest frame and transform to image
        captured_image = Image.fromarray(opencv_image)
        # Convert captured image to photoimage
        photo_image = ImageTk.PhotoImage(image=captured_image)
        label.photo_image = photo_image
        label.configure(image=photo_image)

def select_file():
    filetypes = (('video files', '*.mp4 *.avi *.AVI *.m4p'),)
    filename = fd.askopenfilenames(filetypes=filetypes)
    outputpath = os.path.join(os.getcwd(), "video.mp4")

    # get video and information about input video
    vid = cv2.VideoCapture(filename[0])
    fps = vid.get(cv2.CAP_PROP_FPS)
    ret, frame = vid.read()
    height, width, layers = frame.shape

    # create output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(outputpath, fourcc, fps, (width, height))

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
                x, y = int(x), int(y)
                x2, y2 = boxes[i][2], boxes[i][3]
                x2, y2 = int(x2), int(y2)
                face = frame[x:x2,y:y2]
                coords = (x, y)
                img_boxes = cv2.putText(img_boxes, 'Age: ' + str(age_detector.detect_age(face)), coords, font, scale, color,
                                        thickness, cv2.LINE_AA)
            # write img_boxes image to output video
            output_video.write(img_boxes)
        else:
            break
    player.load(outputpath)
    slider.config(to=player.video_info()["duration"])
    player.play()


def seek(value):
    player.seek(int(value))


def update_duration(event):
    duration = player.video_info()["duration"]
    slider["to"] = duration


def update_scale(event):
    progress_value.set(player.current_duration())


def stop_camera():
    global vid
    global isPlaying
    isPlaying = False
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def read_camera():
    global isPlaying
    global vid
    global font
    global scale
    global color
    global thickness
    if isPlaying:
        _, frame = vid.read()

        boxes = detector.predict(frame)

        # apply boxes to image
        img_boxes = Detector.draw_bounding_boxes(frame, boxes)
        for i in range(boxes.shape[0]):
            x, y = boxes[i][0], boxes[i][1]
            x, y = int(x), int(y)
            x2, y2 = boxes[i][2], boxes[i][3]
            x2, y2 = int(x2), int(y2)
            face = frame[x:x2,y:y2]
            coords = (x, y)
            img_boxes = cv2.putText(img_boxes, 'Age: ' + str(age_detector.detect_age(face)), coords, font, scale, color,
                                    thickness, cv2.LINE_AA)

        # Convert image from one color space to other
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

        # Capture the latest frame and transform to image
        captured_image = Image.fromarray(opencv_image)

        # Convert captured image to photoimage
        photo_image = ImageTk.PhotoImage(image=captured_image)

        # Displaying photoimage in the label
        label_widget.photo_image = photo_image

        # Configure image in the label
        label_widget.configure(image=photo_image)

        # Repeat the same process after every 10 milliseconds
        label_widget.after(10, read_camera)
def open_camera():
    global isPlaying
    global vid
    global font
    global scale
    global color
    global thickness
    if isPlaying:
        read_camera()

    else:
        vid = cv2.VideoCapture(0)
        isPlaying = True
        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        # fontScale
        scale = 1
        # Blue color in BGR
        color = (0, 255, 0)
        # Line thickness of 2 px
        thickness = 2

        # Declare the width and height in variables
        width, height = 800, 600

        # Set the width and height
        vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        open_camera()


# GUI
age_detector=AgeDetector(os.path.join('age_detection','age_models','inception3.onnx'))
root = tk.Tk()
root.title("Age recognition")
root.minsize(800, 600)
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)

tabControl.add(tab1, text='LIVE VIDEO')
tabControl.add(tab2, text='VIDEO FILE')
tabControl.add(tab3, text='DIRECTORY WITH IMAGES')
tabControl.add(tab4, text='HELP')
tabControl.pack(expand=1, fill="both")


# LIVE VIDEO TAB
path = os.path.join('face_detection', 'models', 'best_nano_1.onnx')
# make new detector
detector = Detector(path)

vid = cv2.VideoCapture(0)
isPlaying = True
# font
font = cv2.FONT_HERSHEY_SIMPLEX
# fontScale
scale = 1
# Blue color in BGR
color = (0, 255, 0)
# Line thickness of 2 px
thickness = 2

# Declare the width and height in variables
width, height = 800, 600

# Set the width and height
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

button2 = Button(tab1, text="Stop Camera",
                 command=stop_camera)
button2.pack(side=BOTTOM, fill="x")
button1 = Button(tab1, text="Open Camera",
                 command=open_camera)
button1.pack(side=BOTTOM, fill="x")
label_widget = Label(tab1)
label_widget.pack(side=TOP, fill="x")


# VIDEO FILE TAB
player = TkinterVideo(tab2, height=30)
player.bind("<<Loaded>>", lambda e: e.widget.config(width=800, height=500))
player.pack(side=TOP, fill="x")
play_img = PhotoImage(file="Resources/play.png")
playButton = Button(tab2, image=play_img, width=40, height=40, command=player.play)
playButton.pack(side=LEFT)
pause_img = PhotoImage(file="Resources/pause.png")
pauseButton = Button(tab2, image=pause_img, width=40, height=40, command=player.pause)
pauseButton.pack(side=LEFT)
progress_value = DoubleVar(tab2)
slider = Scale(tab2, from_=0, to=100, orient="horizontal", variable=progress_value, length=900, showvalue=False,
               command=seek)
slider.pack(side=LEFT)
openButton = Button(tab2, text="Select...", command=select_file)
openButton.pack(side=LEFT)
player.bind("<<Duration>>", update_duration)
player.bind("<<SecondChanged>>", update_scale)


# DIRECTORY WITH FILES TAB

images_array = []
iterator = 0

left_img = PhotoImage(file="Resources/angle-left.png")
leftButton = Button(tab3, image=left_img, width=40, height=40, command=previous_image)
leftButton.pack(side=LEFT)
right_img = PhotoImage(file="Resources/angle-right.png")
rightButton = Button(tab3, image=right_img, width=40, height=40, command=next_image)
rightButton.pack(side=RIGHT)
openButton = Button(tab3, text="Select...", command=select_directory)
openButton.pack(side=BOTTOM)

img = Image.open("Resources/placeholder.jpg")
size = 700, 500
img.thumbnail(size,Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)

# Create a Label Widget to display the text or Image
label = Label(tab3, image=img)
label.pack(side=TOP)

# HELP TAB
ttk.Label(tab4, text="A simple application with UI that detects ages of people. Data can be input in 3 ways:\n" +
                     "- directly from the webcam,\n" +
                     "- as a video file,\n" +
                     "- as a folder with images.\n" +
                     "In each scenario the app appends bounding boxes with age labels to faces detected in the " +
                     "data.").grid(column=0, row=0, padx=30, pady=30)


root.mainloop()

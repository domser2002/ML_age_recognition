from tkinter import *
from tkinter import filedialog as fd
from tkVideoPlayer import TkinterVideo
# sample video player code later to be incorporated into gui


def select_file():
    filetypes = (('video files', '*.mp4 *.avi *.AVI *.m4p'),)
    filename = fd.askopenfilenames(filetypes=filetypes)
    player.load(filename[0])
    slider.config(to=player.video_info()["duration"])


def seek(value):
    player.seek(int(value))


def update_duration(event):
    duration = player.video_info()["duration"]
    slider["to"] = duration


def update_scale(event):
    progress_value.set(player.current_duration())


root = Tk()
player = TkinterVideo(root, height=30)
player.bind("<<Loaded>>", lambda e: e.widget.config(width=800, height=500))
player.pack(side=TOP, fill="x")
play_img = PhotoImage(file="Resources/play.png")
playButton = Button(root, image=play_img, width=40, height=40, command=player.play)
playButton.pack(side=LEFT)
pause_img = PhotoImage(file="Resources/pause.png")
pauseButton = Button(root, image=pause_img, width=40, height=40, command=player.pause)
pauseButton.pack(side=LEFT)
progress_value = DoubleVar(root)
slider = Scale(root, from_=0, to=100, orient="horizontal", variable=progress_value, length=900, showvalue=False,
               command=seek)
slider.pack(side=LEFT)
openButton = Button(root, text="Select...", command=select_file)
openButton.pack(side=LEFT)
player.bind("<<Duration>>", update_duration)
player.bind("<<SecondChanged>>", update_scale)
root.mainloop()

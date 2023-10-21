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
        return
    def read_video(self):
        print("reading from video")
        return
    def read_camera(self):
        print("reading from camera")
        return
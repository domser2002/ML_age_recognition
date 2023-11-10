import face_recognition

class FaceRecognizer:
    def recognition(path):
        image = face_recognition.load_image_file(path)
        face_locations = face_recognition.face_locations(image)
        return face_locations
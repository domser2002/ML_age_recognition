import cv2
from simple_image_download import simple_image_download
import face_recognition
import os
from pathlib import Path


# saves "amount" images of people aged "age"
def scrape_images(age, amount):
    if amount == 0:
        return
    query = 'photo of a ' + str(age) + ' year old face'
    response.download(keywords=query, limit=amount)
    d = os.path.join(Path(__file__).parent.absolute(), 'simple_images', query)
    newname = os.path.join(Path(__file__).parent.absolute(), 'simple_images', str(age))
    os.rename(d, newname)


# extracts face images from raw image located in "path"
def extract_face(path):
    img = cv2.imread(path)
    if img is not None:
        face_locations = face_recognition.face_locations(img)
        i = 0
        for coordinates in face_locations:
            (top, right, bottom, left) = coordinates
            cropped = img[top:bottom, left:right].copy()
            cv2.imwrite(path.split('.')[0] + str(i) + '.' + path.split('.')[1], cropped)
            i += 1
    os.remove(path)


# scrapes amount_vector[x] images of people aged x and converts scraped images into face crops
def data_scraping(amount_vector):
    if len(amount_vector) != 100:
        return
    d = os.path.join(Path(__file__).parent.absolute(), 'simple_images')
    response = simple_image_download.simple_image_download()
    for x in range(0, 99):
        scrape_images(x + 1, amount_vector[x], response)
    sd = [f.path for f in os.scandir(d) if f.is_dir()]
    for subdir in sd:
        for filename in os.listdir(subdir):
            extract_face(os.path.join(subdir, filename))
            

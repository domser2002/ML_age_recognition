import cv2
from icrawler.builtin import BingImageCrawler
import face_recognition
import os
from pathlib import Path
import shutil
from imagededup.methods import PHash
from simple_image_download import simple_image_download
from bing_image_downloader import downloader
import csv
import sys


# downloads "amount" images selected by "query" from Bing and saves them in "directory"
def bing1(directory, query, amount):
    old_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'simple_images', query)
    bing_crawler = BingImageCrawler(downloader_threads=4, storage={'root_dir': old_directory})
    bing_crawler.crawl(keyword=query, max_num=amount)
    merge(directory, old_directory, query, "bing1")


# downloads "amount" images selected by "query" from Google and saves them in "directory"
def google(directory, query, amount):
    response = simple_image_download.simple_image_download()
    response.download(keywords=query, limit=amount)
    old_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'simple_images', query)
    merge(directory, old_directory, query, "google")


# downloads "amount" images selected by "query" from Bing and saves them in "directory" (different scraper)
def bing2(directory, new_directory, query, amount):
    downloader.download(query, limit=amount, output_dir=directory, filter='photo')
    old_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), query)
    merge(new_directory, old_directory, query, "bing2")


# merges a specific download directory "old_directory" with the main one "directory"
def merge(directory, old_directory, query, phrase):
    for item in os.listdir(old_directory):
        src_path = os.path.join(old_directory, item)
        mid_path = os.path.join(old_directory, query + phrase + item)
        dst_path = os.path.join(directory, query + phrase + item)
        os.rename(src_path, mid_path)
        shutil.move(mid_path, dst_path)
    os.rmdir(old_directory)


# saves "amount" images of people aged "age"
def scrape_images(age, amount):
    amount *= 2
    bing_amount = min(200, amount)
    google_amount = min(100, amount)
    if age < 13:
        query_x = 'stock image' + str(age) + ' year old child'
    elif age > 17:
        query_x = 'stock image' + str(age) + ' year old person'
    else:
        query_x = 'stock image' + str(age) + ' year old teenage'
    query_n = 'photo ' + str(age) + ' year old face'
    if age > 17:
        query_m = str(age) + ' year old man'
        query_f = str(age) + ' year old woman'
    else:
        query_m = str(age) + ' year old boy'
        query_f = str(age) + ' year old girl'
    queries = [query_n, query_m, query_f, query_x]
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(parent_dir, 'simple_images', str(age))
    os.mkdir(directory)
    for query in queries:
        bing1(directory, query, bing_amount)
    if len(os.listdir(directory)) > amount:
        return
    for query in queries:
        google(directory, query, google_amount)
    if len(os.listdir(directory)) > amount:
        return
    for query in queries:
        bing2(parent_dir, directory, query, bing_amount)


# extracts face images from raw image located in "path"
def extract_face(path):
    img = cv2.imread(path)
    if img is not None:
        face_locations = face_recognition.face_locations(img)
        i = 0
        for coordinates in face_locations:
            (top, right, bottom, left) = coordinates
            if bottom - top >= 100:
                cropped = img[top:bottom, left:right].copy()
                cv2.imwrite(path.split('.')[0] + str(i) + '.' + path.split('.')[1], cropped)
                i += 1
    os.remove(path)


# removes exact and near duplicates of images in a collection in "path"
def remove_duplicated(path):
    phasher = PHash()
    encodings = phasher.encode_images(image_dir=path)
    duplicates = phasher.find_duplicates(encoding_map=encodings)
    for value in duplicates.values():
        for image in value:
            try:
                os.remove(os.path.join(path, image))
            except FileNotFoundError as e:
                print(f"FileNotFoundError successfully handled\n")


# scrapes amount_vector[x] images of people aged x+1 and converts scraped images into face crops
def data_scraping(amount_vector):
    if len(amount_vector) != 100:
        return
    d = os.path.join(Path(__file__).parent.absolute(), 'simple_images')
    if not os.path.exists(d):
        os.makedirs(d)
    for i in range(0, 99):
        if amount_vector[i] > 0:
            scrape_images(i + 1, amount_vector[i])
            remove_duplicated(os.path.join(d, str(i + 1)))
    sd = [f.path for f in os.scandir(d) if f.is_dir()]
    for subdir in sd:
        for filename in os.listdir(subdir):
            extract_face(os.path.join(subdir, filename))


if __name__ == "__main__":
    argumentList = sys.argv[1:]
    if len(argumentList) != 2:
        print('Wrong number of arguments\n')
    else:
        with open(os.path.join(Path(__file__).parent.absolute(), 'dataset/rozklad_utc_wiki.csv'), mode='r') as file:
            csvFile = csv.reader(file)
            rows = list(csvFile)
            vector = [0]*100
            for x in range(int(argumentList[0]), int(argumentList[1]) + 1):
                vector[x - 1] = 500 - int(rows[x][2])
                if vector[x - 1] < 0:
                    vector[x - 1] = 0
            data_scraping(vector)


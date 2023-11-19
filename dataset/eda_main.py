from drive_info import *
from age_histogram import *
from histogram import *
import os
from pathlib import Path

# integration with jupyter notebook probably here (?)

# path to dataset and results
dataset_path = os.path.join(Path(__file__).parent.absolute().parent.absolute(), 'simple_images')
results_path=os.path.join(Path(__file__).parent.absolute(),'results')

# generate age histogram
age_path=os.path.join(results_path,'rozklad.jpg')
if not os.path.exists(age_path):
    files=get_files_from_drive()
    # draw_histogram(files) - file names to fix

# generate wrinkles histogram
wrinkles_path=os.path.join(results_path,'rozklad_krawedzie.jpg')
if not os.path.exists(wrinkles_path):
    wrinkles_data=[0]*101
    for i in range(0,101):
        path=os.path.join(dataset_path,str(i))
        if os.path.exists(path):
            wrinkles_data[i]=wrinkles(path)
    histogram(wrinkles_data,'Średnia gęstość krawędzi na zdjęciach z poszczególnych grup wiekowych','Wiek',
            'Procent pokrycia obrazu przez krawędzie',wrinkles_path)

# generate average pixel color and brightness graph
brightness_path=os.path.join(results_path,'rozklad_jasnosc.jpg')
if not os.path.exists(brightness_path):
    color_data=[0]*101
    brightness_data=[0]*101
    for i in range(0,101):
        path=os.path.join(dataset_path,str(i))
        if os.path.exists(path):
            [color_data[i],brightness_data[i]]=average_pixel_color_and_brightness(path)
    histogram(brightness_data,'Średnia jasność pikseli na zdjęciach z poszczególnych grup wiekowych','Wiek',
              'Średnia jasność',brightness_path)
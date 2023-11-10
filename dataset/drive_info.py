from mega import Mega
from age_histogram import *
from average_pixel import *
from wrinkles import *

# login to Mega drive
mega = Mega()
m = mega.login('wovtap@laltina.store', '#_table_cloth_35')

# get file information
files = m.get_files()
draw_histogram(files)
average_color_graph(files)
average_brightness_graph(files)
wrinkles(files)

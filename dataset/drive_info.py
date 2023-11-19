from mega import Mega
from age_histogram import *
from average_pixel import *
from wrinkles import *

def get_files_from_drive():
    # login to Mega drive
    mega = Mega()
    m = mega.login('wovtap@laltina.store', '#_table_cloth_35')

    # get file information
    files = m.get_files()
    return files

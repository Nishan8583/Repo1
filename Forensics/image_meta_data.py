'''FIRST have to install pillow library, PIL library is not supported anymore
After installing the follwoing code should work fine
NOTE: NOT EVERY IMAGE CONTAINS EXCHANGE IMAGE FILE FORMAT (exif) info'''

from PIL import Image
from PIL.ExifTags import TAGS
meta_data_dict = {}

img_obj = Image.open("path/to/file")
info = img_obj._getexif()  # getting exif data

if info:  # if exif data was returned
    for (tag,value) in info.items():
        decoded = TAGS.get(tag,tag)  # has to be decoded first
        meta_data_dict[decoded] = value

    for key in meta_data_dict:
        if key == 'GPSInfo':
            print "*******GPS INFO FOUND**********\n"
        print key,'     ',':',meta_data_dict[key]


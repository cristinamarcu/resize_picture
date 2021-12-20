import logging
import os
import re
import sys
from PIL import Image


def resize_image(picturePath, max_size):
    image = Image.open(picturePath)
    width = image.size[0]
    height = image.size[1]
    new_width = width
    new_height = height
    if width > height and width > max_size:
        new_width = max_size
        new_height = height * max_size / width
    elif height > width and height > max_size:
        new_height = max_size
        new_width = width * max_size / height
        
    if width != new_width or height != new_height:
        logging.info(f'resizing {picturePath} from {width}x{height} to {new_width}x{new_height}')
        new_image = image.resize((new_width, new_height))
        new_image.save(picturePath)
    else:
        logging.info(f'no need to resize {picturePath} as {width}x{height} is less than {max_size}')

def resize_images_in_folder(max_size, folderPath):
    for folder, subfolders, file in os.walk(folderPath):
        n = len(file)
        print(file)
        imagere = re.compile('([a-z]+).(jpg|png|bmp|jpeg)', re.IGNORECASE)
        for i in range(0, n):
            matchimage = imagere.search(file[i])
            if matchimage:
                logging.info(f'resizing file {file[i]}')
                resize_image(os.path.join(folderPath, file[i]), max_size)
            else:
                logging.warning(f"skipping file {file[i]} because it's not an image")
                pass

"""
This program resizes to a given dimension all the pictures from a folder.
Example usage:
resize_picture.py 300 C:\\folderPath\\
"""
logging.basicConfig(level=logging.INFO)
resize_images_in_folder(int(sys.argv[1]), sys.argv[2])

"""
A simple image division script that creates
a new image file for the four quarters of
each image file in the current directory

Author: Mark Boon
Date: 18/0/2018
Version: 1.0.1
"""

from PIL import Image, ImageTransform
import os


def crop(img, height, width):
    for i in range(2):
        for j in range(2):
            fragment = (j * width, i * height, (j + 1)
                        * width, (i + 1) * height)
            yield img.crop(fragment)


def image_division():
    # look in the current directory
    file_contents = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    count = 0

    for file in file_contents:
        extension = file[-4:]

        if extension == '.png' or extension == '.jpg' or extension == '.gif':
            img = Image.open(file)
            img_width, img_height = img.size
            height = img_height // 2
            width = img_width // 2

            for fragment in crop(img, height, width):
                new_img = Image.new('L', (width, height), 255)
                new_img.paste(fragment)
                new_img.save(count + ".png")
                count += 1


image_division()

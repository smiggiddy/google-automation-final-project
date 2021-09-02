#!/usr/bin/env python3

import os
import sys
from PIL import Image

def convert_image(file_location):
    # Function converts one file from tiff to JPEG

    head, tail = os.path.split(file_location)
    print(head, " ", tail)
    new_file_name = head +'/' + tail[:3] + '.jpeg'
    try:
        if not os.path.exists(new_file_name):
            with Image.open(file_location) as im:
                im.convert("RGB").resize((600,400)).save(new_file_name, "JPEG", quality=100)
                print("Image converted")
        else:
            print(f"File: {tail}.jpg already exists.")
    except OSError:
        print("Something went wrong with the file path. Check params or file type")

def main(): 
    for file in os.listdir("/home/student-03-d4e234470c42/supplier-data/images/"):
        # print(file)
        convert_image("/home/student-03-d4e234470c42/supplier-data/images/" + file)


if __name__=="__main__":
    main()

#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"


def upload_images(path, url):
    #upload all the pictures for the project
    for file in os.listdir(path):
        if file.endswith('.jpeg'):
            #open file and post it to url
            with open(path + file, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
                #raise error message if failed
                r.raise_for_status()

def main():
    upload_images('supplier-data/images/',url)


if __name__ == "__main__":
    main()

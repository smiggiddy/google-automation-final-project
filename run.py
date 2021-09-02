#!/usr/bin/env python3

import requests
import os
import sys
import re

def convert_file(file_location, file):
    #dictionary to load file contents
    review_data = {}
    line_count = 0
    #file contents keys for dictionary
    keys = ['name','weight','description','image_name']

    with open(file_location, mode='r') as fruit:
        for line in fruit.readlines():
            review_data[keys[line_count]] = line.strip()
            if line_count == 1:
                review_data[keys[1]] = int(re.sub("[A-Za-z ]*", "", line))
            line_count += 1 # print(line[:3])
            review_data['image_name'] =  file[:3] + ".jpeg"
    fruit.close()

    return review_data

def post_to_site(fruit_data, url):
    #function handles HTTP post request and sends reviews to website
    #posts incoming review data variable to parameter url
    reviews_post = requests.post(url, json=fruit_data)
    #return an error if unsuccessful
    reviews_post.raise_for_status()
    #otherwise prints successful
    if reviews_post.status_code == 201:
        print("Successfully updated entry: {}".format(reviews_post.status_code))

def list_directory_files(folder_location):
    #loads all files in directory then calls convert function and post to site function
    all_fruit = []
    for file in os.listdir(folder_location):
        data = convert_file(folder_location + file, file)
        all_fruit.append(data)

    return all_fruit

def read_directory_files(folder_location, url):
    #loads all files in directory then calls convert function and post to site function
    for file in os.listdir(folder_location):
        data = convert_file(folder_location + file, file)
        post_to_site(data, url)

def main():
     url = 'http://104.197.41.74/fruits/'
     folder_location = 'supplier-data/descriptions/'
     read_directory_files(folder_location, url)

if __name__== '__main__':
    main()

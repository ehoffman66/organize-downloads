#!/usr/bin/env python3

'''
_author_ = Erik Hoffman
'''

import os
import shutil

user = input("Enter username: ")

img = [".img",".png",".jpg"]
doc = [".xls",".xlsx",".doc",".docx"]

def check_path(file_path):
    '''Check to see if path exists'''
    print(file_path)
    return os.path.exists(path)

path = "/Users/" + user +  "/Downloads/"
if check_path(path):
  files = os.listdir(path)
  for file in files:
    split = os.path.splitext(file)
    if split[1] != "":
      if split[1] in img:
        print("Image")
        shutil.move(path + file, path + "images/")
      elif split[1] in doc:
        print("Doc")
else:
    print("Please put in a valid user")

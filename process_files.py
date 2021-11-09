#!/usr/bin/env python3

'''
_author_ = Erik Hoffman
'''

import os

user = input("Enter username: ")
img = [".img",".png",".jpg"]
doc = [".xls",".xlsx",".doc",".docx"]

def check_path(file_path):
    '''Check to see if path exists'''
    print(file_path)
    return os.path.isfile(path)

path = "/Users/" + user +  "/Downloads/"
if check_path(path):
  files = os.listdir(path)
  for file in files:
    split = os.path.splitext(file)
    if split[1] != "":
      if split[1] in img:
        print("FOUND!")
else:
    print("Please put in a valid user")

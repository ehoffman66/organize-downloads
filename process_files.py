#!/usr/bin/env python3

'''
_author_ = Erik Hoffman
'''

import os
import shutil

user = input("Enter username: ")

file_types = ["img","doc"]
img = [".img",".png",".jpg",".gif",".psd",".raw"]
doc = [".xls",".xlsx",".doc",".docx",".txt","pdf"]

def check_path(file_path):
    '''Check to see if path exists'''
    print(file_path)
    return os.path.exists(file_path)

path = "/Users/" + user +  "/Downloads/"
for types in file_types:
    if not check_path(path + types + "/"):
        os.mkdir(path + types + "/")

if check_path(path):
  files = os.listdir(path)
  for file in files:
    split = os.path.splitext(file)
    if split[1] != "":
      for ftype in file_types:
        print(ftype)
        if split[1] in eval(ftype):
          print("Image")
          shutil.move(path + file, path + ftype + "/")
else:
    print("Please put in a valid user")

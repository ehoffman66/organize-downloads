#!/usr/bin/env python
"""
A quick python program for parsing the contents of a users downloads
folder and sorting them into folders by type.
"""

__author__ = "Erik Hoffman"
__contact__ = "erik.m.hoffman@gmail.com"
__date__ = "2021/11/09"
__deprecated__ = False

import os
import shutil
import sys

user = sys.argv[1]

file_types = ["img","doc","remove","zip"]
img = [".img",".png",".jpg",".gif",".psd",".raw"]
doc = [".xls",".xlsx",".doc",".docx",".txt",".pdf",".json"]
zip = [".zip"]
remove = [".dmg",".exe"]

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
        if split[1] in eval(ftype):
          shutil.move(path + file, path + ftype + "/")
else:
    print("Please put in a valid user")

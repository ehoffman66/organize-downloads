#!/usr/bin/env python
"""
A quick python program for parsing the contents of a users downloads
folder and sorting them into folders by type.
"""

__author__ = "Erik Hoffman"
__contact__ = "erik.m.hoffman@gmail.com"
__date__ = "2021/11/09"
__deprecated__ = False

import os, time
import shutil
import sys
import datetime
from venv import create

if len(sys.argv) == 2:
    user = sys.argv[1]
else:
    print("Please Enter a User")
    quit()

file_types = ["img","doc","remove","comp","data"]
img = [".img",".png",".jpg",".jpeg",".gif",".psd",".raw"]
doc = [".xls",".xlsx",".doc",".docx",".txt",".pdf"]
data = [".json",".csv"]
comp = [".zip"]
remove = [".dmg",".exe"]
path = "/Users/" + user +  "/Downloads/"

def check_path(file_path):
    '''Check to see if path exists'''
    return os.path.exists(file_path)

def create_dir():
    """Create missing directories"""
    for types in file_types:
        if types == "remove":
            continue
        if not check_path(path + types + "/"):
            print(types)
            os.mkdir(path + types + "/")

def move_files():
    """Move files to their correct folder"""
    if check_path(path):
        files = os.listdir(path)
        for file in files:
            split = os.path.splitext(file)
            create_date = os.path.getmtime(path + file)
            create_date = datetime.datetime.fromtimestamp(create_date)
            current_date = datetime.datetime.now()
            if current_date.date() > create_date.date() and split[1] in remove:
                print("File Removed: " + file)
                print(create_date.date())
                os.remove(path + file)
            if split[1] != "":
                for ftype in file_types:
                    if split[1] in eval(ftype):
                        if ftype == "remove":
                            continue
                        shutil.move(path + file, path + ftype + "/")
    else:
        print("Please put in a valid user")

create_dir()
move_files()

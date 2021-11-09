#!/usr/bin/env python3

import os

user = input("Enter username: ")
img = [".img",".png",".jpg"]
doc = [".xls",".xlsx",".doc",".docx"]

path = "/Users/" + user +  "/Downloads/"
files = os.listdir(path)
for file in files:
    split = os.path.splitext(file)
    if split[1] != "":
        print(split[1])
        if split[1] in img:
            print("FOUND!")
            
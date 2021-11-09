import os

user = input("Enter username: ")

files = os.listdir("/Users/" + user +  "/Downloads/")
for file in files:
  print(file)


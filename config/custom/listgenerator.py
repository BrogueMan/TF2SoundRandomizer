import os
import random

con = ""

for path, subdirs, files in os.walk(os.getcwd()):
    for file_name in files:
        if ".wav" in file_name or ".mp3" in file_name or ".ogg" in file_name:
            if(len(path.split('custom\\')) > 1):
                filepath = path.split('custom\\')[1] + "\\" + file_name
                con = con + filepath + "\n"
                print(filepath)
            else:
                con = con + file_name + "\n"
                print(file_name)

with open(os.getcwd() + "//custom_list.txt", 'w') as file:
        file.write(con)
        print("custom_list FILE CREATED")

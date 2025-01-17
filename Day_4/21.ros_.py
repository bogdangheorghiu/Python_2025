


import os
from pprint import pprint


current_directory = os.getcwd()
print("The  currect directory is ", current_directory)

all_filles = os.listdir(current_directory + "/Day 4")
print(type(all_filles))


extensions = ["py", "ipynb"]

filterede_filed = []
for filename in all_filles:
    if filename.endswith(extensions[0]) + filename.endswith(extensions[1]):
        filterede_filed.append(filename)


filterede_filed = sorted(filterede_filed)
print(filterede_filed)

files_to_rename = []
for filename in filterede_filed:
    if filename[1] =="." and filename[0].isnumeric():
        files_to_rename.append(filename)

for filename in files_to_rename:
    os.renam(current_directory + "/" + filename, current_directory + "/0" +filename)
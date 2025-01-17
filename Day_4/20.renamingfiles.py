
# operating sistem
import os
from pprint import pprint

current_directory = os.getcwd()
print("The  currect directory is ", current_directory)
print(type(all_filles))


print(os.listdir(current_directory))

all_filles = os.listdir(current_directory)
print(type(all_filles))

extensions = ["py", "ipynb"]

filtered_file = []
for filename in all_filles:
    if filename.endswith(extensions[0]) or (filename.endswith[1]):
        filtered_file.append(filename)

filtered_file = sorted(filtered_file)
print(filtered_file)



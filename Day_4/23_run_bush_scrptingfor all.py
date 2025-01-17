




import subprocess
import os

current_directory = os.getcwd() 
current_directory =  "Day_4"
all_files = os.listdir(current_directory)
ipynb_file = []

# insatll_command = "pip install ipynb-py-convert"
# subprocess.Popen(insatll_command, shell=True)


ipynb_file = []
for filename in all_files:
    if filename.endswith("ipynb"):
        ipynb_file.append(filename)

for filename in ipynb_file:
    old_file = f"{current_directory}/{filename}"
    new_file = f"{current_directory}/{filename}".replace("ipynb", "py")

    command = f"ipynb-py-convert {old_file} {new_file}"
    print(command)
    subprocess.Popen(command, shell=True)



import os

## path assoluto (True/False)
out = os.path.isabs("lesson#1")
print(out)

import os

## isdir
out = os.path.isdir("C:\\Users")
print(out)

## isfile
out = os.path.isfile("C:\\Users\\serena.sensini\\python.zip")
print(out)

import os

## Get the current working directory (CWD)
cwd = os.getcwd()
print(cwd)

# create a directory with relative path
directory = "test"

parent_dir = ".\\"

# Path
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)

# create a directory with abs path
directory = "test"

parent_dir = "C:\\Users\\serena.sensini\\Documents"

# Path
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)

## Get the list of all files and directories in the specified directory
path = "C:\\Users\\serena.sensini\\Documents"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# print the list
print(dir_list)
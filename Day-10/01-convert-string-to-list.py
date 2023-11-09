import os
import sys
# number = sys.argv[1]
# python3 01-convert-string-to-list.py 1234567890 - give this in the cli to make this to work
# print(number)
folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
# folder_paths = sys.argv[1:]
# print(folder_paths)
for folder_path in folder_paths:
    # print(folder_path) # we transformed this line to the bottom line
    files = os.listdir(folder_path)
    # print(files)
    for file in files:
        # print(os.path.join(folder_path, file)) # we transformed this line to the bottom line
        print(file)
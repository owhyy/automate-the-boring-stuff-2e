import os

for folder_name, subfolders, filenames in os.walk("/home/snooze/books"):
    print("The current folder is " + folder_name)

    for subfolder in subfolders:
        print("SUBFOLDER OF " + folder_name + ": " + subfolder)

    for filename in filenames:
        print("FILE INSIDE " + folder_name + ": " + filename)

    print("")

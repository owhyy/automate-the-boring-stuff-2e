import re, os
from pathlib import Path

# to-do
# 1. open directory
# set path

p = Path(Path.cwd() / "reg_search")
os.chdir(p)
# 2. search for all .txt files
albums_after_twoK = re.compile(r"([a-zA-z.,?!].*2\d{3,4})")
print("Post 2000 albums:\n")
files_txt = p.glob("*.txt")
for f in files_txt:
    file_contents = []
    file = open(f)
    file_contents = file.readlines()
    file_contents = "".join(file_contents)
    # print(file_contents)
    for occurence in albums_after_twoK.findall(file_contents):
        print(occurence)

# for every file in directory:
# if file ends in .txt :
# open file
# read lines
# 3. for every .txt file, match regex
# for every line read pass regex search
# for every successful pattern:
# add it to list of successful patterns
# 4. print the files that have the line
# convert list of patterns to string, and print to console

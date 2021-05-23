import pyperclip, re

phone_regex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))? # any 1+ occurence of (\d\d\d) or \d\d\d
    (\s|-|\.)?        # 0 or 1 of (space or - or .)
    (\d{3})           # next 3 digits
    (\s|-|\.)         # another space or - or .
    (\d{4})           # other 4 
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # zero or one of any number of spaces followed by ext or x or ext. then any number of spaces again, and 2-5 digits
)""",
    re.VERBOSE,  # VERBOSE for easier and nicer separation
)

email_regex = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+ # 1+ alphanumeric characters, including . _ % + and -
    @ # @ symbol
    [a-zA-z0-9.-]+ # 1+ alphanumeric characters including . and _ (for the domain)
    (\.[a-zA-Z]{2,4}) #. something that is a character and 2-4 characters long
    
)""",
    re.VERBOSE,  # VERBOSE for easier and nicer separation
)
text = str(pyperclip.paste())  # paste from clipboard

matches = []  # where we'll copy from after finding matches
for groups in phone_regex.findall(text):  # for every found phone in the text:
    phone_num = "-".join(
        [groups[1], groups[3], groups[5]]
    )  # make a new '-' separated string of the form xxx-xxx-xxxx
    if groups[8] != "":  # if there is any ext:
        phone_num += " x" + groups[8]  # add to xxx-xxx-xxxx one x and the ext:
    matches.append(phone_num)  # add it to list of matches

for groups in email_regex.findall(text):  # for every found email:
    matches.append(groups[0])  # add the email to matches

if len(matches) > 0:  # if you found anything
    pyperclip.copy(
        "\n".join(matches)
    )  # copy it to clipboard and add a \n after every match
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("No phone number or email adresses found.")

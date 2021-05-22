import pyperclip, re

phone_regex = re.compile(
    r"""(
    (\d{3}}|\({3}\))? # any 1+ occurence of (\d\d\d) or \d\d\d
    (\s|-|\.)?        # space and - or .
    (\d{3})           # other 3 digits
    (\s|-|\.)         # another - or .
    (\d{4})           # other 4 
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)""",
    re.VERBOSE,
)

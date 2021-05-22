import re

# phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# mo = phoneNumRegex.search("My number is 415-555-4242.")
# print("Phone number found: " + mo.group())

phoneNumRegexGroup = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mogr = phoneNumRegexGroup.search("My number is 415-555-4242.")
print(mogr.group(1))
print(mogr.groups())
areaCode, mainNumber = mogr.groups()
print(areaCode)
print(mainNumber)

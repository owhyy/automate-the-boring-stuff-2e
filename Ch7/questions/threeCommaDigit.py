import re


three_comma_digit = re.compile(r"^\d{1,3}(,\d{3})*$")
print(three_comma_digit.search("42") == None)
print(three_comma_digit.search("1,234") == None)
print(three_comma_digit.search("6,368,745") == None)

print(three_comma_digit.search("12,34,567") == None)
print(three_comma_digit.search("1234") == None)

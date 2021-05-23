import re

watanabe = re.compile(r"^([A-Z]\w+\s)+Watanabe$")
print(watanabe.search("Haruto Watanabe") == None)
print(watanabe.search("Alice Watanabe") == None)
print(watanabe.search("RoboCop Watanabe") == None)

print(watanabe.search("haruto Watanabe") == None)
print(watanabe.search("Mr. Watanabe") == None)
print(watanabe.search("Watanabe") == None)
print(watanabe.search("Haruto watanabe") == None)

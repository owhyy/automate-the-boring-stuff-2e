import re


sent = re.compile(
    r"(^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)(\.$))",
    re.IGNORECASE,
)
print(sent.search("Alice eats apples.") == None)
print(sent.search("Bob pets cats.") == None)
print(sent.search("Carol throws baseballs.") == None)
print(sent.search("Alice throws Apples.") == None)
print(sent.search("BOB EATS CATS.") == None)

print(sent.search("RoboCop pets cats.") == None)
print(sent.search("ALICE THROWS FOOTBALLS.") == None)
print(sent.search("Carol eats 7 cats.") == None)

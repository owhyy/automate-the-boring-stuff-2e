# madlib generating program.
# probably are wayyy better ways, but even this took sooo long...
import re
import string

to_be_replaced = ("ADJECTIVE", "NOUN", "ADVERB", "VERB")
file = open(f"sentence.txt", "r")
sentence = []
for word in file.readlines():
    sentence += word.split(" ")

sent_strip = [re.sub(r"[^A-Za-z0-9]+", "", x) for x in sentence]

for index, word in enumerate(sentence):
    if word == to_be_replaced[0]:
        sentence[index] = input("Enter an adjective ")
    elif word[:-1] == to_be_replaced[0] and word[-1] in string.punctuation:
        sentence[index] = input("Enter an adjective ") + word[-1]

    elif word == to_be_replaced[1]:
        sentence[index] = input("Enter a noun ")
    elif word[:-1] == to_be_replaced[1] and word[-1] in string.punctuation:
        sentence[index] = input("Enter a noun ") + word[-1]

    elif word == to_be_replaced[2]:
        sentence[index] = input("Enter a adverb ")
    elif word[:-1] == to_be_replaced[2] and word[-1] in string.punctuation:
        sentence[index] = input("Enter a adverb ") + word[-1]

    elif word == to_be_replaced[3]:
        sentence[index] = input("Enter a verb ")
    elif word[:-1] == to_be_replaced[3] and word[-1] in string.punctuation:
        sentence[index] = input("Enter a verb ") + word[-1]


writefile = open(f"madlib.out", "w")
writefile.write(" ".join(sentence))
file.close()
writefile.close()

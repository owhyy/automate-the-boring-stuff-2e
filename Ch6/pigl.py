print("Enter the English message to translate into Pig Latin:")
message = input()

VOWELS = ("a", "e", "i", "o", "u", "y")

pig_latin = []  # holds piglatin sentence
for word in message.split():  # for every word in list from input():
    prefix_non_letters = ""  # stuff that is not a string (punctuation, spaces)

    # separate non-letters at the beginning of the word
    while (
        len(word) > 0 and not word[0].isalpha()
    ):  # while word starts with a non-letter
        prefix_non_letters += word[0]  # add the non-letter to string of non-letters
        word = word[1:]  # word is now everything except first word

        if len(word) == 0:  # why is this line needed? adds nothing to sentence...
            pig_latin.append(prefix_non_letters)
            continue

    suffix_non_letters = ""  # reset string of non-letters
    while not word[-1].isalpha():  # while the character of the word is a non-letter
        suffix_non_letters += word[-1]  # add the non-letter
        word = word[:1]  # word is now first letter

    was_upper = word.isupper()  # remember case
    was_title = word.istitle()

    word = word.lower()  # convert everything to lowercase

    prefix_consonants = ""
    while (
        len(word) > 0 and not word[0] in VOWELS
    ):  # while the word is not "" and does not start with a vowel
        prefix_consonants += word[0]  # prefix is first letter
        word = word[1:]  # continue from the next next letter untill the end

    if prefix_consonants != "":  # if the prefix is a letter
        word += (
            prefix_consonants + "ay"
        )  # word becomes second letter till end + first letter + ay
    else:
        word += "yay"  # otherwise word is second letter till last + yay

    # restore case
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # add any nonletter (the one it the word started with), the modified word and the non-letter the word ends with
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

print(" ".join(pig_latin))  # convert list to string and add spaces
a = "ana"

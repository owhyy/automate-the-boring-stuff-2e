def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):  # check first 3 characters
        if not text[i].isdecimal():  # if they're not numbers
            return False  # then it's not a number
    if text[3] != "-":  # if 4-th char is not a dash
        return False
    for i in range(4, 7):  # same as above but 4-7
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

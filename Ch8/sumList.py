import pyinputplus as pyip


def adds_up_to_ten(numbers):
    numbers_list = list(numbers)  # convert numbers to a list
    for i, digit in enumerate(numbers_list):  # for every digit in the list, + the index
        numbers_list[i] = int(digit)  # convert it to a integer
    if sum(numbers_list) != 10:  # if the sum of numbers in the list is not 10
        raise Exception(
            "The digits must add up to 10, not %s" % (sum(numbers_list))
        )  # error
    return int(numbers)  # return int


response = pyip.inputCustom(adds_up_to_ten)

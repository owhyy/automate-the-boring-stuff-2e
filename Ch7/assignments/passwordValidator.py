import re


def is_strong_password(password):
    tester = re.compile(r"^([a-zA-z0-9]{8})")


# >>> tester = re.compile(r"^((([a-z]+)|([A-Z]+))|([0-9]+))*$")

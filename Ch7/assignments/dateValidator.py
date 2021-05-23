# TO-DO
# 1. regexp for DD/MM/YYYY format
# 2. make days range from 01-31, month from 01-12 and year 1000-2999
# 3. check if date is valid

import re

date_finder = re.compile(r"(^0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/([12][0-9]{3})*$")

date_lists = [
    "29/02/2020",  # leap year
    "28/02/2021",  # non-leap year
    "31/04/2021",
    "15/06/1999",
    "01/13/2003",
    "50/02/2004",
    "19/09/3500",
    "15/10/2334",
]

date = []
for line in date_lists:  # for every line in list of dates:
    group = line.split("\n")  # treat every line separately
    found_date = date_finder.search(line)  # date
    if found_date != None:  # if it's a valid date (between 1->31, 1->12, 1000->2999)
        date.append(found_date.group())  # add it to list of dates


def is_valid_date(date):
    for d in date:
        day = int(d[:2])
        month = int(d[3:5])
        year = int(d[6:])
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30:
                print(str(d) + " is not a valid date")
            else:
                print(str(d) + " is a valid date")

        if month == 2:
            if (year % 4 == 0 and not year % 100 == 0) or (
                year % 100 == 0 and year % 400 == 0
            ):
                if day > 29:
                    print(str(d) + " is not a valid date")
                else:
                    print(str(d) + " is a valid date")
            else:
                if day > 28:
                    print(str(d) + " is not a valid date")
                else:
                    print(str(d) + " is a valid date")
        if (
            month == 1
            or month == 3
            or month == 5
            or month == 7
            or month == 8
            or month == 10
            or month == 12
        ):
            if day > 31:
                print(str(d) + " is not a valid date")
            else:
                print(str(d) + " is a valid date")


is_valid_date(date)

import shutil, os, re

date_pattern = re.compile(
    r"""^(.*?)              # text before the date
        ((0|1)?\d)-         # one+ digits of 0 or 1 for the month
        ((0|1|2|3)?\d)-     # one + 0 or 1 or 2 or 3 digit for the day
        ((19|20)\d\d)       # 19 or 20 + 2 other digits for the year
        (.*?)$              # text after date
        """,
    re.VERBOSE,
)

for amer_filename in os.listdir("."):  # for every filename in current directory
    mo = date_pattern.search(amer_filename)  # search the regexp on the filename

    if mo == None:  # if the regexp did not find anything
        continue  # start go to the next filename

    before_part = mo.group(1)  # stuff before date
    month_part = mo.group(2)  # part of month
    day_part = mo.group(4)  # part of day
    year_part = mo.group(6)  # part of year
    after_part = mo.group(8)  # part after the date

    euro_filename = (
        before_part + day_part + "-" + month_part + "-" + year_part + after_part
    )

    abs_working_dir = os.path.abspath(".")
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
    # shutil.move(amer_filename, euro_filename)

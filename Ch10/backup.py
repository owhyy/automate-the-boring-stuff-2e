import zipfile, os


def backup_to_zip(folder):
    folder = os.path.abspath(folder)  # makes sure folder is absolute

    number = 1  # number which will be in the filename
    while True:
        zipfilename = (
            os.path.basename(folder) + "_" + str(number) + ".zip"
        )  # filename of zip will be foldername + _number + .zip
        if not os.path.exists(zipfilename):  # if
            break
        number += 1

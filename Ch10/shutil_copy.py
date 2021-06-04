import shutil, os
from pathlib import Path

p = Path.home()
print(shutil.copy(p / "spam.txt", p / "some_folder/eggs.txt"))

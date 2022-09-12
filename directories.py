from os import rmdir
from pathlib import Path

my_directory = Path("real_estate")
new_directory = Path('Social')

# Checking Whether or not direectory exists
print(my_directory.exists())

# Creating directory
# my_directory.mkdir()

# rmdir to remove directory
# my_directory.rmdir()

# Rename
# my_directory.rename("Property_dealer")

# iterdir() ilterating over an ilterator (Gen Obj)
# print(new_directory.iterdir())
# for data in new_directory.iterdir():
#     print(list(data))

# List ilterating
# social_data =[data for data in new_directory.iterdir()]
# print(social_data)

# getting only files 
# paths =[data for data in new_directory.iterdir() if data.is_dir()]
# print(paths)

# CAse 1: Searching using a pattern using the asterisk symbol
# paths =[data for data in new_directory.iterdir() if data.is_dir()]
# python_files =[data for data in new_directory.glob("*.py")]
# print(paths)
# print(python_files)

# Case 2: Searching recursively using the rglob() method
python_files =[data for data in new_directory.rglob("*.py")]
print(python_files)
from pathlib import Path

# Creating an obsolete path on windows
# path = Path("C:\\Program Files\\ Python 3")
# path1 = Path(r"C:\Program Files\ Python 3")
# print(path)
# print(path1)

"""Relativ Path"""
# path = Path("users/__init__.py")
# print(path)

#cobining path()
# path_2 = Path("some_files") / Path('user')

# Combining path() objects together with string
path_2 = Path("some_files") / 'ecommerce' / "__init__.py"
print(path_2)
# getting home directory of the current user 
print(Path.home())

#calling the exists method to find out if this file or directory exist or not

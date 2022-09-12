from pathlib import Path
from time import ctime
import shutil
source = Path("property_dealer/property.py")
new_source = Path("property_dealer/app.py")
my_directory = Path("property_dealer/__init__.py")
astronomy = Path("Astronomy")
# Checking wether a files exists or not 
# print(source.exists())

# Rename
# source.rename('property_dealer/app.py')
# removing files 
# new_source.unlink()

# return info about time 
# print(my_directory.stat())
# print(ctime(my_directory.stat().st_atime))
# print(my_directory.read_bytes())

# write bytes
# print(my_directory.write_bytes(b'print("Possibilities into the reality")'))
# print(my_directory.write_text('print("Possibilities into the reality")'))
# print(my_directory.read_text())

# Copying a file to another location
# print(astronomy
# .mkdir())
target_directory = Path('Astronomy')
shutil.copy(my_directory, target_directory)

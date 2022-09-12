from pathlib import Path
from zipfile import ZipFile


#..............Creating a zipFiles ****************
all_z = ZipFile("zip_dir/all.zip", "w")
py_z = ZipFile("zip_dir/py.zip", 'w')

# print(all_z)
# print(py_z)

# Approch one for all files
for path in Path("social").rglob("*.*"):
    all_z.write(path)
all_z.close()

#.........Approcah two... pyfiles
with ZipFile("zip_dir/py.zip", 'w') as pyfiles:
    for path in Path("social").rglob("*.py"):
        pyfiles.write(path)

# showig all files 
with ZipFile("zip_dir/all.zip") as all_files:
    print(all_files.namelist())

# Getting a single files info
with ZipFile('zip_dir/py.zip') as file_info:
    info = file_info.getinfo("social/social.py")
    print(info.file_size)
    print(info.compress_size)
    print(info.orig_filename)
    print(info.__module__)

# Extracting files 
with ZipFile('zip_dir/all.zip') as all_files_z:
    all_files_z.extractall("Extracted")
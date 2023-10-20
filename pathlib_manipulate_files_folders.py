from pathlib import Path
from  datetime import datetime

# p1 = Path('files/2023-10-17.18-38-18.txt')
# p2 = Path('files/test.txt')
# p3 = Path('files')

# #use path object 
# if not p2.exists():
#   with open(p2, 'w') as file:
#     file.write('Content test')

# #print path object attributes
# print(p1.name)
# print(p1.stem)
# print(p1.suffix)

# #iterate through all files in the folder
# for item in p3.iterdir():
#   print(item, type(item))



##rename all files in the folder by adding prefix
# root_dir = Path('files')
# print(Path.cwd())

# file_paths = root_dir.iterdir()

# for path in file_paths:
#   new_filename = "new-" + path.stem + path.suffix
#   new_filepath =path.with_name(new_filename)
#   print(new_filepath)
#   path.rename(new_filepath)



# ##rename all files in the folder with sub folders
# root_dir = Path('files')
# file_paths = root_dir.glob("**/*")

# for path in file_paths:
#   if path.is_file():
#     parent_folder = path.parts
#     subfolders = parent_folder[1:-1]
    
#     new_filename = '-'.join(subfolders) + '-' + path.stem + path.suffix
#     new_filepath = path.with_name(new_filename)
    
#     print(new_filepath)
#     path.rename(new_filepath)



# #extract date when file has been created
# path = Path('files/2022/December/2022-December-a.txt')
# stats = path.stat()

# second_created = stats.st_ctime
# datetime_created = datetime.fromtimestamp(second_created)
# datetime_created_str = datetime_created.strftime("%Y-%m-%d_%H:%M:%S")

# print(second_created)
# print(datetime_created)
# print(datetime_created_str)


# #replace extention .txt -> .csv
# root_dir = Path('files')
# file_paths = root_dir.glob("**/*.txt")

# for path in file_paths:
#   if path.is_file():
#     new_filepath = path.with_suffix('.csv')

#     print(new_filepath)
#     path.rename(new_filepath)


# #create empty files
# root_dir = Path('files')

# for i in range(5,7):
#   filename = 'empty-' + str(i) + '.txt'
#   filepath = root_dir / Path(filename)
#   filepath.touch()
#   print(filepath)


# #zip files
# import zipfile
# root_dir = Path('files')
# archive_path = root_dir / Path('archive.zip')

# with zipfile.ZipFile(archive_path, 'w') as zip:
#   for path in root_dir.rglob('*.txt'):
#     zip.write(path)
#     print(path)
#     path.unlink()


# #unzip files
# import zipfile
# root_dir = Path('files')
# destination_path = Path('.') / Path('destination')

# for path in root_dir.rglob('*.zip'):
#   print(path)
#   with zipfile.ZipFile(path, 'r') as zf:
#     finalpath = destination_path / Path(path.stem)  
#     zf.extractall(path=finalpath)


# #search files in folders
# root_dir = Path('.')
# file_paths = root_dir.rglob('*')

# discovered_files = []
# search_pattern = "2023-10-19"
# for path in file_paths:
#   if path.is_file():
#     if search_pattern in path.stem:
#       print(path.absolute())


# #change content and delete files forever
# root_dir = Path('destination')

# for path in root_dir.glob('*.txt'):
#   with open(path, 'wb') as file:
#     file.write(b'')
#   path.unlink()
import os
from datetime import datetime


mod_Time = os.stat('C:/temp/test.py').st_mtime
print(datetime.fromtimestamp(mod_Time))

mycdir = os.getcwd()
print(os.getcwd())
os.chdir('c:/users/bwbeckwi/desktop')
os.makedirs('Python/Scripts')
print(os.getcwd())
print(os.listdir())
os.removedirs('Python/Scripts')
os.chdir(mycdir)
print(os.getcwd())
print(os.listdir())

for dirpath, dirnames, filenames in os.walk('c:/users/bwbeckwi/desktop'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()

print('')
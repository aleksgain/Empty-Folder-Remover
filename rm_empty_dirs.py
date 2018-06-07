#!/usr/bin/env python
import os, shutil
try:
    from os import scandir
except ImportError:
    from scandir import scandir
def get_size(path):
    size = 0
    for i in os.scandir(path):
        if i.is_dir:
            size += os.path.getsize(i.path)
        else:
            size += i.stat.st_rsize
    return(size/1024/1024)
path = input('Enter the working directory (currently in \'{}\', hit Enter if agree): '.format(os.getcwd()))
if not path:
    path = os.getcwd()
dirs = os.scandir(path)
dir_dict = []
size = input('\nEnter the minimum size for directory to survive (default is 100MB): ')
if not size:
    size = 100
for dir in dirs:
    if os.path.isdir(dir):
        dir_size = get_size(dir)
        if dir_size < size:
            dir_dict.append(dir)
print('\nHere\'s the list of all directories that will be deleted:\n')
for i in dir_dict:
    print(i.path)
if input('\nAre you sure you want to delete all folders smaller than {}MB?\n(Yes/No): '.format(size)).lower() == ('yes'):
    print('\n')
    for i in dir_dict:
        try:
            shutil.rmtree(i)
            print('Removing ',i.path)
        except shutil.Error as err:
            print('Some directories were not deleted.\n{}'.format(err.filename))
else:
    print('\nFolder purge cancelled..')
print('\nAll actions completed, exiting..\n')



'''
What is OS.walk?
It generates the file names in a directory tree by walking the 
tree either top-down or bottom-up.

For each directory in the tree rooted at directory top 
(including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).

dirpath # is a string, the path to the directory.

dirnames 
# is a list of the names of the subdirectories in dirpath (excluding ‘.’ and ‘..’).

filenames 
# is a list of the names of the non-directory files in dirpath.

What is Fnmatch:
The fnmatch module compares file names against 
glob-style patterns such as used by Unix shells.

These are not the same as the more sophisticated regular expression rules.
It’s purely a string matching operation.

fnmatch() compares a single file name against a pattern and 
returns a boolean indicating whether or not they match. 

The comparison is case-sensitive when the operating system uses 
a case-sensitive file system.
'''
#Find all mp3 files
#This script will search for *.mp3 files from the rootPath (“/”)


import fnmatch
import os
 
rootPath = '/'
pattern = '*.mp3'
 
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))

#Search computer for specific files
#This script uses ‘os.walk’ and ‘fnmatch’ with filters to 
# search the hard-drive for all image files

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

for root, dirnames, filenames in os.walk("C:\"):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))

print(matches)
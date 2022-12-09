'''
Getting all files with specific extension
OS.listdir and endswith( )
Find all files that endswith .txt
'''
import os
items = os.listdir(".")

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
print (newlist)
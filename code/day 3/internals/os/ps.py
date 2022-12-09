#moving the system process map into a Python dictionary

import re
import subprocess

args = ['ps', 'aux']
ps = subprocess.Popen(args, stdout=subprocess.PIPE)
processes = ps.stdout.readlines() 
header = re.split('\s+', processes.pop(0))[:-1]
header.remove('COMMAND')

PS = {}
for process in processes:
   columns = re.split('\s+', process)
   if columns[0]!='oracle':
        continue
   PS[int(columns[1])] = {}
   for position, column in enumerate(columns[:9]):
        PS[int(columns[1])][header[position].lower()] = column
        PS[int(columns[1])]['command'] = ' '.join(columns[10:])

from pprint import pprint
print(PS)

'''
Output:
... 
 25892: {'%cpu': '0.0',
       '%mem': '3.9',
        'command': 'xe_w000_XE ', 
        'pid': '25892',
        'rss': '23672', 
        'start': '16:02',
        'stat': 'Ss',
        'tty': '?',
        'user': 'oracle',
        'vsz': '457240'},
  26142: {'%cpu': '2.0',
        '%mem': '0.9',
        'command': 'python proc.py ',
        'pid': '26142',
        'rss': '5732', 
        'start': '16:36',
        'stat': 'S+', 
        'tty': 'pts/2',
        'user': 'oracle', 
        'vsz': '160776'},
  26143: {'%cpu': '0.0',
        '%mem': '0.1',
        'command': 'ps aux ', 
        'pid': '26143',
        'rss': '1100',
        'start': '16:36',
        'stat': 'R+', 
        'tty': 'pts/2',
        'user': 'oracle', 
        'vsz': '108044'}}
    '''
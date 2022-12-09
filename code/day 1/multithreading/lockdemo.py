# Example: bad program: 
from threading import Lock
lock = Lock()

def do_something_dangerous():
    lock.acquire()
    raise Exception('oops I forgot this code could raise exceptions')
    lock.release()       # This is never called  BAD

try:
    do_something_dangerous()
except:
    print('Got an exception')
lock.acquire()
print('Got here')
'''
Clearly lock.release() will never be called, 
causing all other threads calling do_something_dangerous() to 
become deadlocked. In our program, 
this is represented by never hitting the print('Got here') line.
''' 


# To fix above issue:
from threading import Lock
lock = Lock()

def do_something_dangerous():
    with lock:
        raise Exception('oops I forgot this code could raise exceptions')

try:
    do_something_dangerous()
except:
    print('Got an exception')
lock.acquire()
print('Got here')

'''
Individual object profiling to decide which one to use:

import sys
>>> sys.getsizeof({})    #136
>>> sys.getsizeof([])     #32
>>> sys.getsizeof(set()) #112

So list is better.
'''
# pip install memory-profiler
#python -m memory_profiler profiling.py
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_func()

# To profile entire application use guppy package (pip install guppy)
from guppy import hpy
h = hpy()
print(h.heap())


'''
import os, psutil, gc, time    # pip install psutil
l=[i for i in range(100000000)]
print("before calling del ")
print(psutil.Process(os.getpid()).memory_info())
del l
print("With gc.collect() and after calling del")
gc.collect()
print(psutil.Process(os.getpid()).memory_info())
'''
#observe
'''   
     without gc.collect()
...  vms=4102791168 before gc.collect()
...  vms=9007104 after calling del without gc.collect()

    with gc.collect()
... vms=4102774784 before calling gc.collect()
... vms=9072640 after calling gc.collect()

If one also triggers for other objects with a GC, it works from 3.2G -> 0.13G. 
Therefore its memory did not return to OS till a GC did trigger. 
This is how python prepares memory management
 and how to fix memory leak in python.


 mprof package can be used to profile antire application
 with plot using matplotlilb.

 pip install mprof
'''

'''
Profiling:

The exercise of profiling produces a set of statistical measures. 
These statistics enable us to understand how long each part of the code took 
and how many times it was executed.

'''
'''
#timeit
from time import time
start = time()
# your script here
end = time()
print(f'It took {end - start} seconds!')
'''

# importing line_profiler module
from line_profiler import LineProfiler
  
def geek(rk):
    print(rk)
  
rk ="geeks"
profile = LineProfiler(geek(rk))
profile.print_stats()#It gives detailed report on time consumed by a program.
#Timer unit: 4.27198e-10 s

'''
cProfile:
Python includes a built in module called cProfile which is used to measure the execution
 time of a program.cProfiler module provides all information about how long the program
  is executing and how many times the function get called in a program.

'''
# importing cProfile
import cProfile  
cProfile.run("10 + 10")
'''
Output:
3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :1()
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler'
'''
#Code 2  
def f():
    print("hello")
cProfile.run('f()')
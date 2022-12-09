#cprofile

import cProfile
import pandas as pd
print(cProfile.run("pd.Series(list('ABCDEFG'))"))
'''
258 function calls (256 primitive calls) in 0.001 seconds
Ordered by: standard name
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:997(_handle_fromlist)
     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     1    0.000    0.000    0.000    0.000 _dtype.py:319(_name_get)
  ....
  11/9    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1    0.000    0.000    0.000    0.000 {built-in method numpy.array}
     1    0.000    0.000    0.000    0.000 {built-in method numpy.empty}

ncalls: is the number of calls made. When there are two numbers (like 11/9 above), the function recurred. 
The first value is the total number of calls and the second value is the number of primitive or
  non-recursive calls.
tottime: is the total time spent in the given function (excluding time made in calls to sub-functions).
percall: is the quotient of tottime divided by ncalls.
cumtime: is the cumulative time spent in this and all subfunctions. This figure is accurate even for recursive functions.
percall: is the quotient of cumtime divided by primitive calls.
filename:lineno(function): provides the respective data of each function.
'''
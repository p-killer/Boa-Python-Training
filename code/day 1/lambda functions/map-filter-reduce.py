# map-filter-reduce in Python
'''
Map, Filter, and Reduce are paradigms of functional programming. 
it allows to write simpler, shorter code, without neccessarily 
needing to bother about intricacies like loops and branching.

map(func, *iterables)

Where func is the function on which each element in iterables (as many as they are) 
would be applied on. Notice the asterisk(*) on iterables? It means there can be as 
many iterables as possible, in so far func has that exact number as required input arguments.
'''

names = ['murthy', 'raj', 'laxmi', 'kiran']
uppered_names = []

for n in names:
    name_ = n.upper()
    uppered_names.append(name_)

print(uppered_names)

#with map
uppered_names = list(map(str.upper, names))
print(uppered_names)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1,7)))
print(result) #[3.6, 5.58, 4.009, 56.2424, 9.01344, 32.00013]

#with zip
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]
results = list(zip(my_strings, my_numbers))
print(results)

#with lambda without zip
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
print(results)

'''
Filter
While map() passes each element in the iterable through a function and
 returns the result of all elements having passed through the function, filter(), first of all,
  requires the function to return boolean values (true or false) and then passes 
each element in the iterable through the function, "filtering" away those that are false
'''

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))
print(over_75)

#with lambda
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)

'''
Reduce
reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally
 starting with an initial argument. 
'''
from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result) # 68
''' reduce takes the first and second elements in numbers and passes them 
to custom_sum respectively. custom_sum computes their sum and
returns it to reduce. reduce then takes that result and applies it as the first element
 to custom_sum and takes the next element (third) in numbers as the second element 
 to custom_sum. 
It does this continuously (cumulatively) until numbers is exhausted.
'''

import numpy as np
x = np.array([1, 2, 3, 4, 5])
squarer = lambda t: t ** 2
vfunc = np.vectorize(squarer)
vfunc(x)
# Output : array([ 1,  4,  9, 16, 25])


import numpy as np 
x = np.array([1, 2, 3, 4, 5]) 
# Obtain array of square of each element in x 
squarer = lambda t: t ** 2 
squares = np.array([squarer(xi) for xi in x])
print(squares)

squarer = lambda t: t ** 2 
vfunc = np.vectorize(squarer) 
print(vfunc(x))
'''
#timeit
from time import time
start = time()
# your script here
end = time()
print(f'It took {end - start} seconds!')
'''

#Timeit decorator pattern
from time import time
from functools import wraps

def timeit(func):
    """
    :param func: Decorated function
    :return: Execution time for the decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__} executed in {end - start:.4f} seconds')
        return result

    return wrapper

#consume the decorator now
import random
# An arbitrary function
@timeit
def sort_rnd_num():
    numbers = [random.randint(100, 200) for _ in range(100000)]
    numbers.sort()
    return numbers

numbers = sort_rnd_num()

#sort_rnd_num executed in 0.3020 seconds
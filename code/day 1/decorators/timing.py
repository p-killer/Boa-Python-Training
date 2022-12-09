
# Profililng python function

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      
        run_time = end_time - start_time    
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs") #f-string
        return value
    return wrapper_timer

@timer
def task(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

task(1)
task(999)
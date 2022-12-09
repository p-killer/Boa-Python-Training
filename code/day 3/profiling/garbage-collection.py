'''
Memory Management in Python:

>>> x = 5
>>> print(x)
5
>>> del x
>>> print(x)
Traceback (most reent call last):
  File "<mem_manage>", line 1, in <module>
    print(x)
NameError : name 'x' is not defined
'''
import gc
print(gc.get_threshold())
'''
(700, 10, 10)
As you see, here we have a threshold of 700 for the first generation, 
and 10 for each of the other two generations.
We can alter the threshold value for triggering the garbage collection process 
using the set_threshold() method of the gc module:
gc.set_threshold(900, 15, 15)
'''
'''
Perform Manual Memory managment:
>>> def create_cycle():
...     list = [8, 9, 10]
...     list.append(list)
...     return list
... 
>>> create_cycle()
[8, 9, 10, [...]]

Introduction
Memory management is the process of efficiently allocating, de-allocating, and coordinating memory so that all the different processes run smoothly and can optimally access different system resources. Memory management also involves cleaning memory of objects that are no longer being accessed.

In Python, the memory manager is responsible for these kinds of tasks by periodically running to clean up, allocate, and manage the memory. Unlike C, Java, and other programming languages, Python manages objects by using reference counting. This means that the memory manager keeps track of the number of references to each object in the program. When an object's reference count drops to zero, which means the object is no longer being used, the garbage collector (part of the memory manager) automatically frees the memory from that particular object.

The user need not to worry about memory management as the process of allocation and de-allocation of memory is fully automatic. The reclaimed memory can be used by other objects.

Python Garbage Collection
As explained earlier, Python deletes objects that are no longer referenced in the program to free up memory space. This process in which Python frees blocks of memory that are no longer used is called Garbage Collection. The Python Garbage Collector (GC) runs during the program execution and is triggered if the reference count reduces to zero. The reference count increases if an object is assigned a new name or is placed in a container, like tuple or dictionary. Similarly, the reference count decreases when the reference to an object is reassigned, when the object's reference goes out of scope, or when an object is deleted.


The memory is a heap that contains objects and other data structures used in the program. The allocation and de-allocation of this heap space is controlled by the Python Memory manager through the use of API functions.

Python Objects in Memory
Each variable in Python acts as an object. Objects can either be simple (containing numbers, strings, etc.) or containers (dictionaries, lists, or user defined classes). Furthermore, Python is a dynamically typed language which means that we do not need to declare the variables or their types before using them in a program.

For example:

>>> x = 5
>>> print(x)
5
>>> del x
>>> print(x)
Traceback (most reent call last):
  File "<mem_manage>", line 1, in <module>
    print(x)
NameError : name 'x' is not defined
If you look at the first 2 lines of the above program, object x is known. When we delete the object x and try to use it, we get an error stating that the variable x is not defined.


You can see that the garbage collection in Python is fully automated and the programmer does not need worry about it, unlike languages like C.

Modifying the Garbage Collector
The Python garbage collector has three generations in which objects are classified. A new object at the starting point of it's life cycle is the first generation of the garbage collector. As the object survives garbage collection, it will be moved up to the next generations. Each of the 3 generations of the garbage collector has a threshold. Specifically, when the threshold of number of allocations minus the number of de0allocations is exceeded, that generation will run garbage collection.

Earlier generations are also garbage collected more often than the higher generations. This is because newer objects are more likely to be discarded than old objects.

The gc module includes functions to change the threshold value, trigger a garbage collection process manually, disable the garbage collection process, etc. We can check the threshold values of different generations of the garbage collector using the get_threshold() method:

import gc
print(gc.get_threshold())
Sample Output:

(700, 10, 10)
As you see, here we have a threshold of 700 for the first generation, and 10 for each of the other two generations.

We can alter the threshold value for triggering the garbage collection process using the set_threshold() method of the gc module:

gc.set_threshold(900, 15, 15)
Subscribe to our Newsletter
Get occassional tutorials, guides, and jobs in your inbox. No spam ever. Unsubscribe at any time.

Newsletter Signup
Enter your email...
In the above example, we have increased the threshold value for all the 3 generations. Increasing the threshold value will decrease the frequency of running the garbage collector. Normally, we need not think too much about Python's garbage collection as a developer, but this may be useful when optimizing the Python runtime for your target system. One of the key benefits is that Python's garbage collection mechanism handles a lot of low-level details for the developer automatically.

Why Perform Manual Garbage Collection?
We know that the Python interpreter keeps a track of references to objects used in a program. In earlier versions of Python (until version 1.6), the Python interpreter used only the reference counting mechanism to handle memory. When the reference count drops to zero, the Python interpreter automatically frees the memory. This classical reference counting mechanism is very effective, except that it fails to work when the program has reference cycles. A reference cycle happens if one or more objects are referenced each other, and hence the reference count never reaches zero.

Let's consider an example.


>>> def create_cycle():
...     list = [8, 9, 10]
...     list.append(list)
...     return list
... 
>>> create_cycle()
[8, 9, 10, [...]]
The above code creates a reference cycle, where the object list refers to itself. 
Hence, the memory for the object list will not be freed automatically 
when the function returns. The reference cycle problem can't be solved by 
reference counting. However, this reference cycle problem can be solved by 
change the behavior of the garbage collector in your Python application.

To do so, we can use the gc.collect() function of the gc module.
'''
import gc
n = gc.collect()
print("Number of unreachable objects collected by GC:", n)

#example
import sys, gc

def create_cycle():
    list = [8, 9, 10]
    list.append(list)

def main():
    print("Creating garbage...")
    for i in range(8):
        create_cycle()

    print("Collecting...")
    n = gc.collect()
    print("Number of unreachable objects collected by GC:", n)
    print("Uncollectable garbage:", gc.garbage)

if __name__ == "__main__":
    main()
    sys.exit()  
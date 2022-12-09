Python Anti Design Pattens:
=========================
Anti-patterns work just opposite to predefined design pattern. 
Anti-patterns are considered undesirable. 

Important Features of the Anti-Pattern

Correctness
Anti-patterns break  code into the smaller chunks so that we can do the wrong things. 

Below is the simple example of accessing a private member outside of the class.

class Student(object):  
    def __init__(self, name, age):  
        self._name = name  
        self._age = age  
r = Student('Puran',26)  
# direct access of protected member  
print("age: {:d}".format(r._age))   # Error


Maintainability
 maintainable code  is easy to understand, easy to debug, and can make the changes when required. 
 Anti-patterns make the program hard to maintain. 

 Importing a module can be a suitable example of maintainability. 
 A module consists of many useful predefined functions to perform a particular task. 
Python has many predefined modules and libraries, which make the program easy and maintainable. 


import math  
x = math.floor(y)  

import multiprocessing as mp  
pool = mp.pool(8)  

Readability
Anti-patterns create complexity in the code so that code becomes hard to read and, understand. 
Programmers can make the common mistake that makes code less readable. 

These common mistakes include not using the zip() method to iterate over a pair of lists,
 asking for permission instead of forgiveness, not using the dict comprehension, 
 using type() to compare types, etc.


nums = [1, 2, 3]  
letters = ["A", "B", "C"]  
  
for num_val, letters_value in zip(nums, letters):  
    print(nums, letters_value)  

zip() method to compare the list pair. It is good practice. 
We used the for loop on the zip(nums, letters) function on the list pair. 
Python will automatically assign the first variable as the next value and the second variable 
as the second list's next value.

Security
As we know that, Python is a high-level, dynamic-typed language, which means the 
user can change the behavior of his code and even can execute the code at runtime. 
Uses of exec can create the security issue in the code.


s = "print(\"Hi!, Murthy\")"  
exec s   # Bad Practice  

#Good Practice
def print_hello_world():  
    print("Hi!  Murthy")  
  
print_hello_world()  

Performance
 We can obtain the large performance using the appropriate functions and libraries. 
 Performance can be affected if we do not use iteritems() to iterate over a large dictionary 
 or use the key in the list to check if keys are contained in the list. 
 
 s = set([1, 2, 3, 4])  
  
if 4 in s:  
    print("The number 4 is in the list.")  
else:  
    print("The number 4 is NOT in the list.")  

In the above code, we have changed the list into the set. 
It is much efficient behind the scene. 
In the list, Python will compare each number with the targeted number 
but using the set; it can directly access the targeted number.

Few Important Anti Pattern in Python:
-----------------------------------

Not Using with to open files:
--------------------------
It is a bad practice not to using with statement while open the file. 
We need to remember closing the file via calling the close() function 
when processing it. If we close the file explicitly, there could be a chance 
of exceptions before the resource is closed. So we should open the file 
using the statement because it implements the context management protocol 
that releases the resource. 

#Bad Practice

new_file = open('some-file.txt', 'r')  
# do something exciting  
new_file.close()  

#Good Practice

with open('some-file.txt', 'r') as fd:  
    data = fd.read()  
  # do something exciting  

Using Debugger in Production Code:
--------------------------------
 When we debug the code and found the bug, we may leave the debugger in the production code. 
 It can affect the behavior of the code.
 It is highly recommended to audit the code to eliminate invocation of debugger before checking it.

Not using literal syntax to initialize empty list/dict/tuple
---------------------------------------
When we initialize the empty list by calling list() than using the empty literals,
 it make the program relatively slow. 
 So it is recommended to use the empty literal to declare list, dictionary, and tuple. 
 
 #Bad Practice
my_list = list()  
# Add something to this empty list  

#Good Practice
my_list = []  
# Add something to this empty list  



Unnecessary use of list/dict/set Comprehension:
---------------------------------------------
Python provides the functions such as all, any, enumerate, iter, itertools.cycle, itertools.accumulate, 
which can directly work with the generator expression. 
We don't need to use comprehension with these methods.
 The all() and any() function is also to provide the short-circuiting, 

Unnecessary use of Python Generators:
We don't need to use the generator's expression within a call to dict, list, or set because
 these three have the comprehension. 
 
 So it is recommended to use comprehension instead of generators. 

#Bad Practice
squares = dict((i,i**2) for i in range(1,10))  

#Good Practice
squares = {i: i**2 for i in range(1,10)}  

Avoid item() method to iterate over a dictionary:
--------------------------------------------
The item() method of the dictionary returns an iterable with the key-value tuples. 
The tuple can be unpacked using for loop. It is a simple, dynamic, and recommended approach.

#Bad Practice:

for code in country:  
    name = country [code]  
    # do something with name  

#Good Practice

for code, name in country.items():  
    # do something with name  
    pass  
else clause on loop without a break statement


Python provides the facility to use the else statement with the loop. 
The else block is executed when the loop is empty and eventually loop becomes
 empty after its execution. This may seem the intended behavior, 
 but this is not the intended behavior most of the time. 
 So we should use the break statement in the loop if we are using the else with Python loop.

#Bad Practice

def search_number(list, searched_number):  
    for i in list:  
        if i == searched_number:  
            print("This list has the searched number")  
    else:  
        print("This list does NOT has the number")  
search_number(range(10), 5)  

#Good Practice

def search_number(list, searched_number):  
    for i in list:  
        if i == searched_number:  
            print("This list has the number")  
            break  
    else:  
        print("This list does NOT have the number")  

search_number(range(10), 5)  

Using Unpythonic loop:
-----------------------
To get items from list we always do "Creating a loop that uses an incrementing index to 
access each element of the list within the loop". 
This is not a good way to accessing each element in a list.
 We should use enumerate() function. 

#Bad Practice

list1 = [1,2,3]  
# creating index variable  
for i in range(0,len(list1)):  
    # using index to access list  
    ele = list1[i]  
    print(i,ele)  

#Good Practice

list = range(10)  
for i, ele in enumerate(l):  
    print(i, ele)  

Assigning a lambda expression to a variable:
---------------------------------------
The Python lambda function is also known as the anonymous function,
 and that is the biggest advantage over the def function. 
 Being anonymous, the lambda method can be assigned to any larger expression. 
 The assignment of the lambda method elements the benefit of the lambda function.
  If it requires assigning the lambda method to a variable, then create an equivalent 
  method using the def statement. 

#Bad Practice

fun = lambda y: 3 * y  

#Good Practice

def fun(y): return 2*y  

Method could be a function:
-------------------------
When a class method doesn't contain any reference of the class (self) and is not preceded by the
 @staticmethod, it will raise "Method could be a function" error. 
 This error is not so serious but we should check the code to determine the function 
 really needs to be a class method. 

#Bad Practice

class Rectangle:  
    def __init__(self, width, height):  
        self.width = width  
        self.height = height  
        self.area = width * height  
    # should be preceded by @staticmethod here or must a class variable  
    def area(width, height):  
        return width * height  

#Good Practice

class Rectangle:  
    # clarifies that this is a static method and belongs here  
    @staticmethod  
    def area(width, height):  
        return width * height  
Or

class Rectangle:  
    @classmethod  
    def print_class_name(cls):  
        # "class name: Rectangle"  
        print("class name: {0}".format(cls))  

    =================================================================
Object-Oriented Pattern
The object oriented pattern is the most common type of design pattern, 

In this method, we create an object and particular class and use the class functionality 
using that defined class's object. 

The oops concepts consist of the following component.

Class
Object
Constructor
Inheritance
Encapsulation
Polymorphism

Class
Class is the blueprint of the object; it contains methods and constructors. 
We use the class keyword to define the class. 

class MyClass:  
    # I have created a new class'"  
    pass  

Object

The object is used to access the class attributes. We can create the class object as follows.

Class Employee:  
           # This is employee class  
           salary = 20000  
           def display(self):  
                       print("The salary is: ", self.name)  
  
# creating an object of employee class  
emp = Employee()  
# displaying the employee salary  
emp.display()  

Constructors
Constructors are special methods that automatically call whenever a new object of that 
class is instantiated. 

They are started with the double underscore __ and called special functions. 
Constructor is defined as __int__() function. It is used to initialize all the variables.

Example -

class Employee:  
    def __init__(self, name, age):  
         
self.name = name  
        self.age = age  
  
    def disp_data(self):  
        print("The employee details: ", self.name, self.age)  
  
# Create a new Employee object  
num1 = Employee("Murthy", 25)  
num1.disp_data()  

Inheritance
Inheritance is the process of derived the property of one class to another class. 

The class that derived another class's property is known as subclass or child class and 
class that derived by another class is called the parent class or base class.

Inheritance provides the reusability of the code.

Example -

class Bird:    
    def speak(self):    
        print("Bird speak")    
#child class Dog inherits the base class Animal    
class Dog(Bird):    
    def bark(self):    
        print("dog barking")    
d = Dog()    
d.bark()    
d.speak()  

The self Parameter
The self works in Python same as the "this" in C++. 
It refers to the current class of function, and we can access data in the class function. 
It works as the variable but won't invoke data.

Example -

Class Employee:  
def __init__(self, name):  
           self.name = name  
def display(self):  
           print(self.name)  
emp = Employee('Murthy')        
print(temp.name)  
emp.display()  

Encapsulation
Unlike C++, Python doesn't support keywords like public, protected, and private to 
define data accessibility. By default, all data in Python is public. 
But it provides the facility to define any method or variable private. 
We can use the "__" to hide its property in front of the variable or method. 

Example -   
class Employee:  
def __init__(self, name, age):  
           self.__name = name  
           self.age = age  
  
def display(self):  
           print(self.name)  
           print(self.age)  
emp = Employee('Murthy')        
print(emp.name)  #error
print(emp.age)  

Example -

class Employee:  
    def __init__(self, name, age):  
               self.name = name # public member  
               self.__age = age # private member  
  
    def display(self):  
               print(self.name)  
               print(self.age)  
emp = Employee('Murthy', 53)             
print(temp.name)  
print(emp._Employee__age) # Accessing private data  


Polymorphism
Polymorphism is one of the most important aspects of oops concepts. 
Python is a dynamic-typed language and tracks the variable types. 
Polymorphism is used to achieve many things in the same way.

Example -

a = 10  
b = 20  
print(a + b)  
c = "Murthy"  
print(c + b)  

Output:
30
Murthy20
The 'add' operation is supported not only by the integer but also the string. 
This is a simple example of polymorphism.

Many operations and functions in Python are polymorphic. 
So as long as we use the polymorphic operators and functions, polymorphism 
will exist even if we don't have this purpose.

Advantages of Object-Oriented Pattern
------------------------------------
It supports the dynamic-typed binding, which means an instance of a class can be changed 
       dynamically at runtime.

Python supports the multiple inheritances and operator overloading with
      an advanced definition that some OOPs language don't have.

Python oops concept doesn't support the private, public and protected keyword because it 
      creates some complexity in the syntax. As Python's inventor, Guido Van Rossum, said, 
      "Abundant syntax brings more burden than help." We can reuse the code using the inheritance.

Polymorphism provides flexibility in the program. Using polymorphism, 
      we can create the same method in the parent class, and it would work in all child classes.

It provides effective problem-solving. OOPs, the concept allows us to break-down the 
     code into bite-size problems that we can then solve.
     ======================================================
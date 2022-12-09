'''
    Singleton design pattern is one of the Credential Design Pattern and it is easiest to implement. 
    It is a way to provide one object of a particular type. 
    It is used to describe the formation of a single 
    instance of class while offering a single global access point to the object.

    Eg: DBConnection

    It prevents the creation of multiple objects of the single class. 
    The newly created object will be shared globally in an application.

    Motivation:    
      Singleton design patterns are specially used in application 
      types that need mechanisms over access to a mutual resource.

   Implementation:
  To implement the singleton pattern, we use the static method. 
  We create the getInstance() method that can return the shared resources. 
  When we call the static method, either it gives the unique singleton object or an 
  error singling an instantiated object's existence.

It restricts to create the multiple objects of a defined class and maintain integrity.

Application:
Singleton patterns solves the most occurring problems such as logging, 
caching, thread pools, and configuration setting 
and often used in conjunction with the Factory design pattern.
'''
class BankSingleton:  
   __instance__ = None  
  
   def __init__(self):  
        if BankSingleton.__instance__ is None:  
           BankSingleton.__instance__ = self  
        else:  
           raise Exception("Instance is already created... sorry")  
  
   @staticmethod  
   def get_instance():  
       # We define the static method to fetch instance  
       if not BankSingleton.__instance__:  
           BankSingleton()  
       return BankSingleton.__instance__  
  
# Creating an object of above defined class.  
bank= BankSingleton()  
print('First :',bank)  
  
same_bank = BankSingleton.get_instance()  
print('Second :',same_bank)  
  
another_bank = BankSingleton.get_instance()  
print('Third:',another_bank)  
  
new_bank = BankSingleton()  
print('new Bank:',new_bank)  
#------------------------------------------
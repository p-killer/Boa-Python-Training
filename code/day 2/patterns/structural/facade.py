'''
Facade:
Façade is a structural design pattern which provides the simpler interface to a library or 
complex set of classes. The word Façade is simply referred to an outer lying interface of 
complex patterns that contains several sub-systems. It is a very important part defined 
by the Gangs of Four design patterns. In the simple word, it defines the higher level interface 
that any subsystem can use.

The main façade class keeps track which subsystem is responsible for a request.
This design pattern helps in communicating with the subsystem easily to the client.

Advantages:
Façade method helps us to isolate our code from the complexity of a subsystem.
It provides the loose coupling between the client and the subsystems.
It makes the testing process easy since it contains convenient methods for common testing task.
'''

"""Facade pattern with an example of Order pizza"""  
  
class Ordering:   
   #Subsystem 1  
  
   def order(self):   
      print("Ordering")   
  
  
class Preparing:   
   #Subsystem 2  
  
   def prepare(self):   
      print("Preparing...")   
  
  
class Delivering:   
   #Subsystem 3  
  
   def deliver(self):   
      print("Delivering...")   
  
  
class Operator:   
   '''Facade'''  
  
   def __init__(self):   
      self.ordering = Ordering()  
      self.preparing = Preparing()   
      self.delivering = Delivering()  
  
   def completeOrder(self):  
      self.ordering.order()  
      self.preparing.prepare()  
      self.delivering.deliver()  
  
""" main method """  
if __name__ == "__main__":   
  
   op = Operator()  
   op.completeOrder()   
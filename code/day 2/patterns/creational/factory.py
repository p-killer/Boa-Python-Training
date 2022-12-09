'''
Factory Design Pattern
A factory design pattern is one of the types of Creational Design Pattern that allows us to use an 
interface or a class to create an object to instantiate. 
The factory method offers us the best way to create an object.
 In this method, objects are created without revealing the logic to the client. 
To create a new type of object, the client uses the same common interface.

Factory methods are very useful in adding new types of product without distributing 
the existing client code. (Polymorphism)
It avoids the tight coupling between the products and the creator classes and objects.

Bank application factory methods:
  - SavingAccount
  - CurrentAccount
  - HomeLoan
'''
class French_Language:   
  
   #it will return the french version    
   def __init__(self):     
      self.translations = {"book": "voiture", "phone": "biclothtte","cloth":"clothtte"}   
  
   def localize(self, msg):    
      """change the message using translations"""  
      return self.translations.get(msg, msg)   
  
class Spanish_Language:   
   #it will return the spanish version  
  
   def __init__(self):   
      self.translations = {"book": "libro", "phone": "teléfono","cloth":"paño"}  
  
   def localize(self, msg):   
      #change the message using translations  
      return self.translations.get(msg, msg)   
  
class English_Language:   
   """Simply return the same message"""  
  
   def localize(self, msg):   
      return msg   
  

def Factory(language ="English"):     
   """Factory Method"""  
   localizers = {   
      "French": French_Language,   
      "English": English_Language,   
      "Spanish": Spanish_Language,   
   }     
   return localizers[language]()   
  

if __name__ == "__main__":     
    fr = Factory("French")   
    en = Factory("English")   
    sp = Factory("Spanish")   
  
    message = ["book", "phone", "cloth"]   
  
    for m in message:   
      print(fr.localize(m))   
      print(en.localize(m))   
      print(sp.localize(m))   
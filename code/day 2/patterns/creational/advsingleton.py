# Double Checked Locking singleton pattern   
import threading   
class Single_Checked(object):   
  
   # resources shared by each and every   
   # instance   
  
   __single_acq_lock = threading.Lock()   
   __singleton_instance = None  
  
   # define the classmethod   
   @classmethod  
   def instance(cls):   
  
      # check for the singleton instance   
      if not cls.__singleton_instance:   
         with cls.__single_acq_lock:   
            if not cls.__singleton_instance:   
               cls.__singleton_instance = cls()   
  
      # return the singleton instance   
      return cls.__singleton_instance   
  
# main method   
if __name__ == '__main__':   
  
   # create class A   
   class A(Single_Checked):   
      pass  
  
   # create class B  
   class B(Single_Checked):   
      pass  
  
a1,a2= A.instance(), A.instance()   
b1,b2= B.instance(), B.instance()   
  
 
print('a1 : ',a1)   
print('a2 : ', a2)   # a1 and a2 are same
print('b1 : ', b1)   
print('b2 : ', b2)  
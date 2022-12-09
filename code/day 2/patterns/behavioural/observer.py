'''
An observer design pattern is a behavioral design pattern where objects are 
represented as observers that wait for an event to trigger.
 When the new event is triggered, the multiple observers catch these events.

The event source (or object) attaches to the subject. 
Whenever the change is performed in the subject, it is notified by the observer. 
It follows the one to many approaches between the objects so that one change in 
the subject will reflect in all of its dependents and be updated automatically.

Advantages:
It is quite flexible to set up the relationship at runtime between the objects.
With the Open/Closed Principle's help, we can introduce the new subscriber class without 
    making a change in the publisher's code.
This method carefully describes the coupling existing between the objects and the observer.


Applications:
The observer method should be used if there are multiple dependencies on the state of one object. 
It follows the one to many dependencies, which means any change in the object state will 
reflect the attached object (in case of loose coupling).

This method is used to send notifications, emails, messages etc. When we subscribe to any particular
 website, we notify you of any new events on that website.

The object should be coupled tightly. If there is loose coupling in objects, the change in one 
state will reflect in another object.

The subscriber list is dynamic, which means subscribers can join and drop the 
subscription when they want.
'''
import threading  
import time  
import pdb  
  
  
class Downloader_Class(threading.Thread):  
  
    def run(self):  
        print('Current Task Downloading')  
        for i in range(1, 6):  
            self.i = i  
            time.sleep(2)  
      
        return 'Hi!  I am Murthy... Download done'  
  
  
class Working_Class(threading.Thread):  
    def run(self):  
        for i in range(1, 6):  
            print('Working_Class running: %i (%i)' % (i, dow.i))  
            time.sleep(1)  
            dow.join()  
  
            print('Task Completed')  
  
  
dow = Downloader_Class()  
dow.start()  
  
time.sleep(1)  
  
wor = Working_Class()  
wor.start()  
  
wor1 = Working_Class()  
wor1.start()  
  
t3 = Working_Class()  
t3.start()  
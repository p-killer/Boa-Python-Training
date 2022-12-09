''' fork of os module will not work in windows. Try this code in lynux.

'''
# in windows
import multiprocessing
 
def myProcess():
  print("{} Just performed X".format(multiprocessing.current_process().name))
 
def main():
  childProcess = multiprocessing.Process(target=myProcess, name='My-Awesome-Process')
  childProcess.start()
  childProcess.join()
 
if __name__ == '__main__':
  main()

'''
import os
'''
def parent_child():
    n = os.fork()
  
    # n greater than 0  means parent process
    if n > 0:
        print("Parent process and id is : ", os.getpid())
  
    # n equals to 0 means child process
    else:
        print("Child process and id is : ", os.getpid())
          
# Driver code
parent_child()
'''
import os

def child():
   print('\nA new child ',  os.getpid())
   os._exit(0)  

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("parent: %d, child: %d\n" % pids)
      reply = input("q for quit / c for new fork")
      if reply == 'c': 
          continue
      else:
          break

parent()
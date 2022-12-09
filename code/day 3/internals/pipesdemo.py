''' pipe and fork of os module will not work in windows. try in lynux 

'''
import os, sys

print ("The child will write text to a pipe and ")
print ("the parent will read the text written by child...")

# file descriptors r, w for reading and writing
r, w = os.pipe() 

processid = os.fork()
if processid:
   # This is the parent process 
   # Closes file descriptor w
   os.close(w)
   r = os.fdopen(r)
   print( "Parent reading")
   str = r.read()
   print ("text =", str)  
   sys.exit(0)
else:
   # This is the child process
   os.close(r)
   w = os.fdopen(w, 'w')
   print ("Child writing")
   w.write("Text written by child...")
   w.close()
   print ("Child closing")
   sys.exit(0)
'''


   # importing os module 
import os
  
  
# Create a pipe
r, w = os.pipe()
  
# The returned file descriptor r and w
# can be used for reading and
# writing respectively.
  
# We will create a child process
# and using these file descriptor
# the parent process will write 
# some text and child process will
# read the text written by the parent process
  
# Create a child process
pid = os.fork()
  
# pid greater than 0 represents
# the parent process
if pid > 0:
  
    # This is the parent process 
    # Closes file descriptor r
    os.close(r)
  
    # Write some text to file descriptor w 
    print("Parent process is writing")
    text = b"Hello child process"
    os.write(w, text)
    print("Written text:", text.decode())
  
      
else:
  
    # This is the parent process 
    # Closes file descriptor w
    os.close(w)
  
    # Read the text written by parent process
    print("\nChild Process is reading")
    r = os.fdopen(r)
    print("Read text:", r.read())
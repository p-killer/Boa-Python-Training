Detecting the current platform is as easy as reaching to a predefined
string in the os module. 

The following example illustrates the outcome on Oracle Linux 6.1 and 
also shows the default path separator for this OS.

>>> import os
>>> os.name 
‘posix’
 >>> os.sep
 ‘/’

 A list of all Oracle’s environment variables is accessible through os.environ. 
  The following example makes use of an inline generator expression:

  >>> import os 
>>> oracle_vars = dict((a,b) for a,b in os.environ.items() if a.find('ORACLE')>=0)
>>> from pprint import pprint
 >>> pprint(oracle_vars) 
 {'ORACLE_HOME': '/u01/app/oracle/product/11.2.0/xe', 'ORACLE_SID': 'XE'}

 '''
 it is like : 
            SELECT key, value 
            FROM os.environ 
            WHERE key LIKE ‘%ORACLE%’
 '''

 os.getcwd()            
    - Gets the current working directory from OS

os.chdir(path)
    - Change directory to the given path

os.chroot(path)
    - Change the  root path for the current Python process to path

os.chown(path, uid, gid)
    - Same as chmod Linux command (uid and gid are numbers)

os.listdir(path)
    - List files and directories under the given path

os.mkdir(path, mode)
    - Creates directory under given path with octal permissions set to mode (0777 by default)

os.remove(path)
    - Deletes a file under path

os.rmdir(path)
    - Removes the directory under path

os.rename(path, newpath)
    - Renames path to newpath

os.stat(path)
    - Shows attributes of path using the OS stat() call

os.walk(path, topdown, onerror, followlinks)
    - Returns generator returning tuples of (path, directories, files) for the filesystem tree under path

    see walk.py code:

OS Process functions
-----------------------

os.abort()
    - Sends SIGABRT to the current Python process

os.exec*(path, arg1...argN, environ)
    - Family of exec* functions to replace the current process with the one specified by path, optionally providing command line arguments and environment variables

os.kill(pid, signal)
    - Sends signal to a given pid

os.nice(value)
    - Changes the current process’s nice value

os.popen(command, mode, buffersize)
    -Opens an unnamed pipe to a given command, 
    effectively enabling further interaction with the process; 
    mode denotes the pipe open handle attribute (‘r’ for read by default)

os.spawn*(mode, path, environ)
    - Runs the program under path in a new process 

os.system(command)
    - This runs a new process defined by the command using OS system() call;
     available on Unix and Windows

ps.py code : watch it

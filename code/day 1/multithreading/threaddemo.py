import threading,time

print("Start of a program")

def longRunningTask():
    x=1
    print("Doing complex work in background")
    while(True):
        x +=1
        #do your work here (backup,uploding,procesing....)
        if(x==5):
            break;
    time.sleep(5)

treadObj=threading.Thread(target=longRunningTask)
treadObj.start()
print("I am waiting for task to complete")
treadObj.join()
print("All work done")

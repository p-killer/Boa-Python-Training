import threading, time
print('Start of program.')

def takeANap():
    x=1
    print("Doing complex work in background")
    while (True):
        x += 1
        if (x == 5):
            break
    time.sleep(5)

    print('Background work completed')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('I am waiting for child to complete the task')

import asyncio

# definition of a coroutine
async def coroutine_1():
    print('coroutine_1 is active on the event loop')
    print('coroutine_1 yielding control. Going to be blocked for 4 seconds')
    await asyncio.sleep(4)
    print('coroutine_1 resumed. coroutine_1 exiting')

# definition of a coroutine
async def coroutine_2():
    print('coroutine_2 is active on the event loop')
    print('coroutine_2 yielding control. Going to be blocked for 5 seconds')
    await asyncio.sleep(5)
    print('coroutine_2 resumed. coroutine_2 exiting')

# this is the event loop
loop = asyncio.get_event_loop()
# schedule both the coroutines to run on the event loop
loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2()))


'''
Some points to note

Calling a coroutine definition does not execute it.
 It initialises a coroutine object. 
 You await on coroutine objects, not coroutine definition

Event loop runs tasks, not coroutine objects directly. 
Tasks are a wrapper around coroutine objects. 
When you write await coroutine_object you essentially schedule a 
wrapper task to be run on the event loop immediately.

asyncio.sleep is a coroutine as well, provided by the asyncio library. 
asyncio.sleep(2) initialises a coroutine object with a value of 2 seconds.
 When you await on it, you give control of the event loop to it. 
 Sleep coroutine is smart and does not block the loop.
  It immediately releases control, simply asking the loop to wake it 
  up after the specified time. 
  When the time expires, it is given back the control and it immediately 
  returns, thereby unblocking its caller 
  (in the above example coroutine_1 or the coroutine_2).

The above example had three different types of coroutines that ran on 
the event loop — coroutine_1, coroutine_2and asyncio.sleep. 
However, four different tasks ran on the loop, corresponding to the 
following coroutine objects — coroutine_1() and coroutine_2() scheduled 
, asyncio.sleep(4) scheduled at line 8 and asyncio.sleep(5) 
scheduled.



'''
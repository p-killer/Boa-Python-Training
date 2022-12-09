
# decorators wrap a function, modifying its behavior.
def my_decorator(func):
    def wrapper(): # inner function
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper #returning a function



@my_decorator
def invoke():
    print("Murthy")

invoke()

''' write custom function and take func as paramter which user wants to invoke
then write wrapper function to perform house keeping task and return
customsied funtion, which will be exucuted by python runtime
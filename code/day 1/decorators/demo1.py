''' Decorators: '''

def say_hello(name):
    return f"Hello {name}"

def appreciate(name):
    return f"Yo {name}, You are great!"

def greet(ptr): # Higher order functions
    '''logging'''
    return ptr("Murthy")

print(greet(say_hello)  
print(greet(appreciate))




















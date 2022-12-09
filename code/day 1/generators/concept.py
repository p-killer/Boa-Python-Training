#Generators
def square_numbers(nums):
    for i in nums:
        yield (i*i)            # so no return as we are returning generator

my_nums = square_numbers([1,2,3,4,5])
print(type(my_nums))  # class 'generator'
print(next(my_nums))  # 1 
print(next(my_nums))  
#---------------------------------------


# Generators to improve performance and efficient memory usage
alist = [4, 16, 64, 256]

# Find square root using the list comprehension
out = [a**(1/2) for a in alist]
print(type(out))
print(out) 
for i in out:
   print(i)

# Use generator expression to calculate the square root for above code (use () )
out = (a**(1/2) for a in alist)
print(out)     #<generator object <genexpr> at 0x03074F70>
print(next(out))  
print(next(out)) 

#----------------------------------------

#CustomGenerators  Internally uses __iter__ and __next__ in yield
def topfive():
    n=1
    while n <=5:
        sq=n*n
        yield sq
        n +=1

values=topfive()
for i in values:
    print(i)

#------------------------------


# Generator next() Method Demo
#
alist = ['Python', 'Java', 'C', 'C++', 'CSharp']
def list_items():
    for item in alist:
        yield item

gen = list_items()
iter = 0
while iter < len(alist):  
    print(next(gen))
    iter += 1
print(iter)

# Generator For Loop Demo
gen = list_items()   # convert list to generators for fast access
for item in gen:
    print(item)
#-----------------------------------------


#--------------------------------------------------
# Find All Prime Numbers Using Generator
def find_prime():
    num = 1
    while True:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
        num += 1

for ele in find_prime():
    print(ele)

#-------------------------------------------------

# Chain Multiple Operations Using Generator Pipeline
# 
def find_primenew():
    num = 1
    while num < 100:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
        num += 1

def find_odd_prime(seq):
    for num in seq:
        if (num % 2) != 0:
            yield num

a_pipeline = find_odd_prime(find_primenew())

for a_ele in a_pipeline:
    print(a_ele)
#------------------------------------------------    

    
def fibonacci(xterms):
    # first two terms
    x1 = 0
    x2 = 1
    count = 0

    if xterms <= 0:
       print("Please provide a +ve integer")
    elif xterms == 1:
       print("Fibonacci seq upto",xterms,":")
       print(x1)
    else:
       while count < xterms:
           xth = x1 + x2
           x1 = x2
           x2 = xth
           count += 1
           yield xth

fib = fibonacci(5)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
#----------------------------------------




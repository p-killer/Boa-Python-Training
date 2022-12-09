nums=[1,5,2,3]
print(nums[1])    
for i in nums:
    print(i)  # internally for loop uses iterator  

it=iter(nums)
print(type(it))  #class 'list_iterator'
print(it.__next__())    #1
print(it.__next__())     #5
print(next(it))     # 2   
print(next(it))    #3
print(next(it))
# if no more items are there then stopIteration exception raised
#---------------------------------------------

#convert tuple to generator using iter  (Iterator)
cubes = (1, 8, 27, 64, 125, 216)

cube = iter(cubes)
print(next(cube))
print(next(cube))
print(type(cube))     #class 'tuple_iterator

#------------------------------------------------

class Head:
    def __init__(self):
        self.num=1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=5:
            val=self.num
            self.num +=1
            return val
        else:
            raise StopIteration

values=Head()
#]]=[[print(values.__next__())
for i in values:
    print(i)
#-----------------------------------

#custom iterator
class natural_numbers:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        if self.max == self.number:
            raise StopIteration
        else:
            number = self.number
            self.number += 1
            return number

numbers = natural_numbers(10)
i = iter(numbers)
print("# Calling next() one by one:")
print(next(i))
print(next(i))
#--------------------------

#Generators  Internally uses __iter__ and __next__ in yield
def topfive():
    n=1
    while n <=5:
        sq=n*n
        yield sq
        n +=1

values=topfive()
for i in values:
    print(i)



    pandas cheet sheet
#Lambda functions are called single line functions
# can I pass a function as parameter to other function

add5=lambda x : x+5

print(add5(10))

square=lambda x:x*x
print(square(5))

#list class contains sort,filter,find,map....


alist=['learn','python','step','by','step']
output=list(map(lambda x:x.upper(),alist))
print(output)


list1=[("eggs",5.25),("honey",9.5),('carrots',1.4)]
list1.sort(key =lambda x:x[1],reverse=1)
#True=1  False=0
print(list1)


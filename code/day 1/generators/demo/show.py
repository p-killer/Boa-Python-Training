
#() will return generator
gen_nums = (x*x for x in [1,2,3,4,5])       #with generators comprehension using () instead of []
print(list(gen_nums))
print(type(gen_nums))   # generator


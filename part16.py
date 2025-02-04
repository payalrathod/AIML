import types,collections
issubclass(types.GeneratorType, collections.Iterator) #returns true

'''
#generator
def square(n):
    for i in range(n):
        yield i*i
#print(square(3))
for i in square(3):
    print(i)

 difference:
> to create iterator we use iter()
> to create generator we use fun along with yield keyword
> generator uses yield keyword as it saves local variable value
> generator in python helps to write fast and compact code
> iterator is much more memory efficient
> iterator uses next keyword

'''
#iterable
'''
lst = [1,2,3,4]
for i in lst:
    print(i)
#iterator
iterable = iter(lst)

#for i in iterable:
#   print(i)
#print(next(iterable))
#print(next(iterable))
#print(next(iterable))
try:
    print(next(iterable))
except StopIteration:
    print("completed")
'''



'''assert statement

num = 10
assert num >= 10

try:
    numm = int(input("enter number"))
    assert numm%2 == 0
    print("even number")
except AssertionError:
    print("enter even number")
'''


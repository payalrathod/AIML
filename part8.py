# lambda function
def addi(a, b):
    return a + b
print(addi(4, 5))

addit = lambda a,b: a+b
print(addit(10,14))

def even(num):
    if num%2 == 0:
        return True
    else:
        return False
print(even(13))

even1 = lambda num1: num1%2==0
print(even1(12))

def addition(x,y,z):
    return x+y+z
print(addition(1,2,3))

addition1 = lambda x,y,z: x+y+z
print(addition1(1,3,4))


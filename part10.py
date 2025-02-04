# list comprehension
lst1 = []


def lst_sq(lst):
    for i in lst:
        lst1.append(i * i)
    return lst1


print(lst_sq([1, 2, 3, 4, 5, 6]))

lst = [1, 2, 3, 4, 5, 6, 7, 88, 23, 45]
pr = [i * i for i in lst]
print(pr)

i: int
pr1 = [i * i for i in lst if i % 2 == 0]
print(pr1)

print("Hello everyone")


def greeting(name):
    return "Hello {}. Welcome here".format(name)

print(greeting("Payal"))

def wel(fname,lname):
    return "Welcome {fname1} {lname} here".format(lname=lname,fname1=fname)
print(wel("Annie","Marie"))

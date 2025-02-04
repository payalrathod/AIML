def evenodd(num):
    # num = 24
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


evenodd(24)


def helwr():
    print("Hello World")


helwr()


def helwr():
    return "Hello World2"


val = helwr()
print(val)


def addNo(num1, num2):
    return num1 + num2


val = addNo(12, 11)
print(val)


# positional argument = name
# keyword argument = age
def hello(name, age=12):
    print("my name {} and age {}".format(name, age))


print(hello('payal'))


def hello1(*args, **kwargs):
    print(args)
    print(kwargs)


hello1("pay1", "ray1", age=12, dob=1999)

lst = ['pay', 'ray']
dicti = {'age': 12, 'dob': 1999}
print(hello1(*lst, **dicti))

mylist = [1, 2, 3, 4, 5, 6, 7]


def evenodd(tsil):
    even = 0
    odd = 0
    for i in tsil:
        if i % 2 == 0:
            even = even + i
        else:
            odd = odd + i

    return even, odd


print(evenodd(mylist))

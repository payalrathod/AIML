# is vs ==
lst = ["kri", "abc", "def"]
lst2 = ["kri", "abc", "def"]
print(lst2==lst)
print(lst is lst2)
a= "kjh"
b= "saw"
print(a==b)

lst=lst2
print(lst is lst2)

lst[0] = "abc"
print(lst)
print(lst2)

# decorators
# function copy
'''
def wel():
    print("asfsreg rrtddfr")


welc = wel()
del wel
welc
#wel()

#closures

def abc(msg):
    #msg = "Hey all!"
    def subabc():
        print("welcome here")
        print(msg)
        print("Please subscribe")
    return subabc()
abc("Hey all! 2")

print("  ")

#decorators
def abc(func):
    def subabc():
        print("welcome here 2")
        #func()
        func("horse is an animal")
        print("Please subscribe 2")
    return subabc()
abc(print)


def abc(func):
    def subabc():
        print("welcome here 2")
        print(func([1, 2, 3, 4, 5, 6, 78, 9, 10]))
        print("Please subscribe 2")

    return subabc()


abc(len)



def abc(func):
    def subabc():
        print("welcome here 2")
        func()
        print("Please subscribe 2")

    return subabc()


@abc
def chann():
    print("this is video")

# abc(chann)


'''
# eval function
print(eval("5*5"))
print(eval("5*5+7/2"))

# print(eval(input("enter expression: "))) #len([1,2,34,5])  sum([1,2,3,4])

def sum_ev(num):
    return num ** 2


print(sum_ev(3))
print(eval("sum_ev(4)"))
'''
eval: parse python expression; compile into byte code;
evaluate python expression; it will return result
'''
var = compile("5*5","<string>","eval")
print(var)
print(eval(var))

#global parameter
x=10
print(eval('x+50+x**2', {"x":x}))

x=8
z=4
print(eval('5+z*3+x/2',{"x":x,"z":z}))

print(eval("a+b+c",{"a":100,"b":2000,"c":30}))
print(eval("x<z"))


print(" ")

# multiple inheritance
class A:
    def method1(self):
        print("method A")


class B(A):
    def method1(self):
        print("method B")

    def method2(self):
        print("method2 B")


class C(A):
    def method1(self):
        print("method C")


class D(B, C):
    def method1(self):
        print("method D")
        C.method1(self)
        B.method1(self)
        A.method1(self)


d = D()
d.method1()
print(" ")
d.method2()
print(" ")
B.method1(d)
print(" ")
A.method1(d)

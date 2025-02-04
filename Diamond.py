class A:
    def meth(self):
        print("class A")
class B(A):
    # pass
    def meth(self):
        print("class B")
class C(A):
    def meth(self):
        print("class C")
class D(C, B): # if B is first so B will print
    pass

d = D()
d.meth()
class vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return 'Vector (%d,%d)' %(self.a,self.b)
    
    def __add__(self,other):
        return vector(self.a+other.a, self.b+other.b)
v1=vector(3,7)
v2=vector(9,2)
print(v1+v2)

#by super keyword
class A():
    def foo(self):
        print("A")
class B(A):
    def foo(self):
        print("B")
        super(B,self).foo()
class C(A):
    def foo(self):
        print("C")
        super(C,self).foo()
class D(B,C):
    def foo(self):
        print("D")
        super(D,self).foo()
d=D()
d.foo()
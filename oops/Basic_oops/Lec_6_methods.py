class Test:
    @classmethod
    def m1(cls):
        print(id(cls))

print(id(Test))
t= Test()
t.m1()

class test:
    def __init__(self) -> None:
        print('-'*20)
        self.a=20
        self.b=4
    def m1(self):
        self.c=4

t1=test()
t1.d =40 #adding instance variable from outside class
t1.m1()
print(t1.__dict__)

#Items vary from object to objects

t2=test()
t2.m1()
print(t2.__dict__)
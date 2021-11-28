class Test:
    a=10
    def __init__(self) -> None:
        Test.b=20

    @staticmethod
    def value_2():
        Test.d=3
    @classmethod
    def value_1(cls):
        cls.c=30
        del Test.b
     
t = Test()
Test.g=100
t.value_1()
print(Test.__dict__)

print('-'*80)

class Static:
    # @staticmethod
    def add(a,b):
        print('sum is ' ,a+b)

s = Static.add(1,2);
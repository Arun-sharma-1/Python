class Test:
    def __init__(self) -> None:
        self.__x = 10

    def __m1(self):
        print('This is private method ')

    def m2(self):
        print(self.__x)
        self.__m1()


T = Test()
T.m2()
# print(T.__x) not possible
# T.__m1() not possible to access private members outside the class
print(T._Test__x) #this is the new name allocated to private var, we can access outside from the class 

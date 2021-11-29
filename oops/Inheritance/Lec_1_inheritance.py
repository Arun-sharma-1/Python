# SYNTAX FOR INHERITANCE
'''class P:
    def __init__(self) -> None:
        print('parent class constructor ')

    def m1(self):
        print('Parent class method ')


class C(P):
    def m2(self):
        print('Child class method ')


# c1 = C()
# c1.m2()
# c1.m1()

class P:
    def __init__(self) -> None:
        print('parent class constructor ')

    def m1(self):
        print('Parent class method ')


class C(P):
    def m2(self):
        self.m1()
        print('Child class method ')


# c1 = C()
# c1.m2()
# c1.m1()
'''

# if name of both method become same then in that conditon we us super


class P:
    def __init__(self) -> None:
        print('parent class constructor ')

    def m1(self):
        print('Parent class method ')


class C(P):
    def m1(self):
        super().m1()
        print('Child class method ')


c1 = C()
c1.m1()

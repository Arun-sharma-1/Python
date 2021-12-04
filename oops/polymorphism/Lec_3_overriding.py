# METHOD OVERRIDING
class P:
    def marry(self):
        print('Arrange marrige ')


class C(P):
    def marry(self):
        # super().marry()
        print('Love Marrige')  # overriding value of parent class


C1 = C()
C1.marry()


# CONSTRUCTOR OVERRIDING

class P:
    def __init__(self) -> None:
        print('Parent class constructor ')


class C(P):
    def __init__(self) -> None:
        # super().__init__()
        print('Child class constructor ')


c1 = C()

print('-'*30)

# SUPER METHOD WITH CONSTRUCTOR AND METHOD


class P:
    def display(self):
        print('This can also be called with the help of super ')


class C(P):
    def display(self):
        super().display()


c1 = C()
c1.display()

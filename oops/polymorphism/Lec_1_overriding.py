#IF OBJECT BELONG TO SAME CLASS
class Book:
    def __init__(self,pages) -> None:
        self.pages= pages
    def __add__(self,other):
        return self.pages+other.pages
b1 = Book(12)
b2=Book(21)
print(b1+b2)

#IF OBJECT BELONG TO DIFFERENT CLASS
class Employee:
    def __init__(self,salry) -> None:
        self.salarypermonth=salry

    def __mul__(self,other) -> None:
        return self.salarypermonth*other.onedaysalary
class Worker:
    def __init__(self,salry) -> None:
        self.onedaysalary=salry

e = Employee(200)
w=Worker(20)
print('Total salary: ',e*w)
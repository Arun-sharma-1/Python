class Employee:
    def __init__(self, ename,  esal) -> None:
        self.name = ename
        self.salary = esal

    def display(self):
        print(self.name)
        print(self.salary)


class Manager:
    def increment(emp):
        emp.salary+=100
        emp.display()

emp = Employee('arun',1)
Manager.increment(emp)



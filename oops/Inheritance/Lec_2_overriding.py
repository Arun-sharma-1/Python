class Emplyoee:
    def __init__(self, name, salary, deptno) -> None:
        self.Empname = name
        self.Empsalary = salary
        self.EmpDeptno = deptno

    def show_data(self):
        print('Empname={}\nEmpsalary={}\nEmpdeptno={}\n'.format(
            self.Empname, self.Empsalary, self.EmpDeptno))


class Salesman(Emplyoee):
    def __init__(self, name, salary, deptno, comm) -> None:
        self.commision = comm
        super().__init__(name, salary, deptno)

    def show_data(self): #overriding used for new defination
        super().show_data()
        print(self.commision)


s = Salesman('arun', '1lac', 1, 20000)
s.show_data()

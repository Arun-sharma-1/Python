# class Emplyoee:
#     def __init__(self,name,salary,deptno) -> None:
#         self.Empname=name 
#         self.Empsalary=salary 
#         self.EmpDeptno=deptno

    
#     def show_data(self):
#         print('Empname={}\nEmpsalary={}\nEmpdeptno={}\n'.format(self.Empname ,self.Empsalary, self.EmpDeptno))

# class Salesman(Emplyoee):
#     def __init__(self, name, salary, deptno ,comm) -> None:
#         super().__init__(name, salary, deptno)
#         self.commision=comm


# s=Salesman('arun','1lac',1,20000)
# s.show_data()
# print(s.commision)

class human:
    def __init__(self,name,dob) -> None:
        self.name = name;
        self.dob=dob

class coder(human):
    def __init__(self , name ,dob, fav_lag) -> None:
        super().__init__(name,dob)
        self.fav_lag=fav_lag
    def show_data(self):
        print(self.name , self.fav_lag)

C = coder('arun','31-10-2001','python')
C.show_data()



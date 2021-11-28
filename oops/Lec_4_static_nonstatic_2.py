
class Employee:
    totalemployee=0
    def __init__(self, empno ,empname, salary,deptno) -> None:
        self.Empno=empno;
        self.EmpName=empname
        self.Salary=salary;
        self.Deptno=deptno
        Employee.totalemployee+=1
    
    def show_Employee(self):
        print('Employee Name: {} \nEmployee NO: {} \nSalary: {} \nEmplyoee dept: {}\n'.format(self.EmpName ,self.Empno ,self.Salary ,self.Deptno))

emp1=Employee(1,'arun','1lac',121)
emp1.EmpName='changed'                  #we can access directly
emp2=Employee(2,'sharma','1.5lac',111)

# emp1.show_Employee()
list=[emp1,emp2]

for item in list:
    item.show_Employee()

print('Total employee :' , Employee.totalemployee)
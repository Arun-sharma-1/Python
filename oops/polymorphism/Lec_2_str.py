class Student:
    def __init__(self,name,salary) -> None:
        self.name=name;
        self.salary=salary
    def __str__(self) -> str:
        return 'Name and salary {} {}: '.format(self.name,self.salary)
    #we have to return string only when we are returnin multiple parametes 

s1=Student('Arun',1000)
print(s1)
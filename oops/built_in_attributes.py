#built-in attributes
class employee:
    
    def __init__(self,n,s):
        self.name=n
        self.salary=s
    def disp(self):
        print("Name is:",self.name)
        print("Salary is:",self.salary)
#class documntation
print("employee.__doc__:",employee.__doc__)

#class name
print("Class name is:",employee.__name__)

#classs module
print("Class module is:",employee.__module__)

#base classes
print("Base classes:",employee.__bases__)

#dictionary containing class namespace
print("Ditionary containing namespace",employee.__dict__)
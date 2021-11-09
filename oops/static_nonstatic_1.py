class Test:
    staticvariable=0;
    instancevariable=0
     #class and static variables are same 
    def __init__(self) -> None:
        print('Constructing the object of first class')
        self.instancevariable+=1;
        Test.staticvariable+=1;
        self.classvariable+=1;

t1=Test()
print('After creating 1st object ')
print('Instance variable: ', t1.instancevariable)
print('static variable :', t1.staticvariable)


print()

t2=Test();
print('After creating 2nd variable ')
print('Instance variable: ', t2.instancevariable)
print('static variable :', t2.staticvariable)


print('static variable using class referene ', Test.staticvariable)

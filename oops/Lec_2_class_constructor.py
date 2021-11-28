class Name:
    def __init__(self, firstname, middlename, lastname):  # constructor
        self.Firstname = firstname
        self.Middlename = middlename
        self.lastname = lastname


class Student:
    def __init__(self, rollno, sname, course) -> None:
        self.Rollno = rollno
        self.Studentname = sname
        self.Course = course

# Student1=Student(1,Name('arun','kumar','sharma'),'cse')
# Student2=Student(2,Name('ram','kumar','sha') , 'ece')


n1 = Name('arun', 'kumar', 'sharma')
Student1 = Student(1, n1, 'cse')
Student2 = Student(2, Name('ram', 'kumar', 'sha'), 'ece')   


# print('Direct :',Student1.Rollno)
# print('Direct :',Student.__Rollno__)

std = [Student1, Student2]
for s in std:
    print('Roll-no:  {} \nstudent name: {} {} {} \ncourse {} \n'
          .format(s.Rollno, s.Studentname.Firstname, s.Studentname.Middlename, s.Studentname.lastname, s.Course))

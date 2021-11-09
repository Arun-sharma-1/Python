class Data:

    def __init__(self, name, rollno, isstudent) -> None:
        self.Name = name
        self.Rollno = rollno
        self.IsStudent = isstudent
        self.on = False

    # Method =>     Difference between function and method is due to self
    def change_something(self):
        self.IsStudent = False
        self.on = True
    


d1 = Data('Arun', 67, True)
print(d1.on)

d1.new_var=1.22
print(d1.new_var)

# d1.change_something()
# print(d1.on)
# print(d1.IsStudent)


# print(d.Name)
# print(d1.IsStudent)
# print('Name: {0.Name}  Rollno: {0.Rollno}    =   Name: {1.Name} Rollno: {1.Rollno} ' .format( d1, d2))

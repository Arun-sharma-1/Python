class Name:
    def __init__(self, firstname, middlename, lastname): #constructor
        self.Firstname = firstname
        self.Middlename = middlename
        self.lastname = lastname
N=Name('arun','kumar','sharma')
print(hasattr(N,"firstname"))
print(getattr(N,"Firstname"))
setattr(N,"Firstname","ravan")
print(getattr(N,"Firstname"))

# delattr(N,"Firstname")
# print(getattr(N,"Firstname"))

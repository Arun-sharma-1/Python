class AgeSet:
    def __init__(self, age=0):
        self._age = age

    # getter method
    def get_age(self):
        return self._age

    # setter method
    def set_age(self, x):
        self._age = x


pkj = AgeSet()

# setting the age using setter
pkj.set_age(int(input("set the age using setter: ")))

# retrieving age using getter
print(pkj.get_age())

print(pkj._age)

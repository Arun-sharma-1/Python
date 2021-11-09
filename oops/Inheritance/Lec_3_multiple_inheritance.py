class Father:
    def FathersProperty(self):
        print("Fathers property")
class Mother:
    def Mothersproperty(self):
        print("Mothers Property ")

class Child(Father, Mother):
    def property(self):
        print("Child will get ")
        super().FathersProperty()
        super().Mothersproperty()

c=Child()
c.property()

class Grandparents:
    def land(self):
        print("property given by grandparents ")
class Parents(Grandparents):
    def Home(self):
        print("HOme given by parents")

class Child(Parents):
    def vehicle(self):
        print("vehicle own by child ")
    def land(self): #overriding
        super().land()
        print('property is used by me for business')

c=Child()
c.land()
c.Home()
c.vehicle()
    
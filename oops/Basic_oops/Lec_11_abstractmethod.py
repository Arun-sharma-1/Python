from abc import ABC, abstractmethod


from abc import abstractmethod
# class Vechile:
#     @abstractmethod
#     def getnoofWheels(self):
#         pass


class Vechile(ABC):
    @abstractmethod
    def getnoofWheels(self):
        pass

    # def new(self):
    #     pass


class Auto(Vechile):
    # pass if i do only pass then it will show error because i have to implement above fn i declared Vechile(ABC)
    def getnoofWheels(self):
        return 9


a = Auto()
print(a.getnoofWheels())

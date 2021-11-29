# class Engine:
#     def useEngine(self):
#         print('Engine specific funtionality ')

# class Car:
#     def __init__(self) -> None:
#         self.engine = Engine()

#     def usecar(self):
#         print('car funtionality...')
#         self.engine.useEngine()

# c1 = Car()
# c1.usecar()

print('-'*40)


class Car:
    def __init__(self, cname, cno, cmodel) -> None:
        self.cname = cname
        self.cno = cno
        self.cmodel = cmodel

    def car_info(self):
        print(
            f'Car name : {self.cname}\nCar-No : {self.cno}\nCar-Model : {self.cmodel} ')


class Employee:
    def __init__(self, name, car) -> None:
        self.name = name
        self.car = car

    def display_info(self):
        print('Employee-Name:{} '.format(self.name))
        print('Car info : ')
        self.car.car_info()


C = Car('honda-city', 1234, 2017)
E1 = Employee('Arun', C)
E1.display_info()

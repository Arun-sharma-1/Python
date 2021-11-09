# class myclass():
#     pass

# O=myclass()
# print(dir(O))

# class object(): #inbuilt class
#     pass

# o=myclass()
# print(dir(o))

class Myerror(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

raise Myerror(' unknown error occured ! pls restart the program ')
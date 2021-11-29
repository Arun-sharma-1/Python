import gc
import sys
# class point:
#     def __init(self,x=0,y=0): #constructor
#         self.x=x
#         self.y=y
#     def __del__(self):# destructor
#         class_name=self.__class__.__name__
#         print("class",class_name,"destroyed")
#     def show(self):
#         print("x=",self.x,"y=",self.y)
# pt1=point()
# pt2=pt1

# print(id(pt1))
# print(id(pt2))

# del pt1

#pt1.show()
# pt2.show()


class Test:
    def __init__(self) -> None:
        print('Constructor execution...')

    def __del__(self):
        print('Destructor Execution..')

t1 =Test()
t2 = t1
print(sys.getrefcount(t1)) #3 = t1, t2 ,self
# del t2 ,t1
print('End of program ')

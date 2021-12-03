import time
import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())

# gc.enable()
# print(gc.isenabled())


class Test1:
    def __init__(self) -> None:
        print('Constructor created ')

    def __del__(self):
        print('Cleanup activities are going on with the help of destructor: ')


t = Test1()
t = None  # del t
time.sleep(1)
print('End of applications ')

print('-'*50)


class Test2:
    def __init__(self) -> None:
        print('Constructor created ')

    def __del__(self):
        print('Cleanup activities are going on with the help of destructor: ')


t1 = Test2()
t2 = Test2()
#At this stage by default garbage collection is turned on 
gc.disable()
print('End of program')

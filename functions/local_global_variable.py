''' 
a=10
print(id(a))
x=globals()['a']  # This will take acces of global variable
print(x)
print(id(x))

globals()['a']=100
print(a)
print(id(a))
'''
fruit={1:'apple', 2:'orange'}
laptop={1:'dell',2:'acer'}
a=laptop.copy()
print(a)
print(type(a))
laptop[2]='hp'
print(laptop)
a=laptop.get(4,'not found')
print(a)


#HOW TO MODIFY A GLOBAL VARIABLE 
enemy = 1
def fn():
    global enemy
    enemy+=1
    return enemy
print(fn())

#IMPORTANT CONCLUSION ABOUT GLOBAL VARIABLE
a=77
def f1():
    print(a)
    global a #error
    a=99
    print(a)

f1()
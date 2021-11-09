'''data1=10
def check():
    data1=1
    print(data1)
    return data1;

def check2():
    global data1;
    data1=100
    print(data1)
    return data1;

print(data1)
check()
check2()
print(data1)


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
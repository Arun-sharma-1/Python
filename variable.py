#named place in memeory
x=2
y=3
print(x+y)
x=10 # now value of x is updated to 10
print(x+y)
# print( _ + 1)   not working
# underscore give the value of privious output 
# z   
# print(z)
# z is not defined so it is an error

name="string"
print(name)
# print(name+"is working")
print(name[0]) # first characther of that string
# print(name[10])  erro-->string index out of scope 
print(name[-1])
print(name[0:3])
print(name[1:4])
print(name[1:3])
print(len(name))
print("\n")
print("Address of variable ")
num=4
print(id(num))  # this is the address of num 
name="arun"
print(id(name))
print("\n")
print("INTERCHANGING OF DATA")
a=4
b=2
a=b;
print(id(a))
print(id(b)) 
# address of both the variable will become same 
print(a)
print(id(2))
print("\n")
print("HOW TO KNOW TYPE OF VARIABLE")
P=3.3
print(type(P))



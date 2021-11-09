numbers= "1,2,3,4,5"
print(type(numbers)) # type is string coz no comma after " "
# x=int(numbers)   THIS IS WRONG 
# print(type(x))

# numbers=input("Enter values of numbers with seperators ")
seperators=""
for char in numbers:
    if not char.isnumeric():
        seperators+=char
print(seperators)
# print(sum(numbers))  this will not work 
# The split() method splits a string into a list.   
x=numbers.split()
print(x)
a=1.1
l1=[1,a,3,4]
print(sum(l1))
 

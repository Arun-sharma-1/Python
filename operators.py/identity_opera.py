""" 
check the address of two variable and return true or false
1.is
2.is not 

"""

a=10
b=10
print(id(a) ,id(b))
print(a is b)

b='10'
print(a is b)
print(a is not b)



x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

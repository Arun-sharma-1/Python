import math
#square of a no 
x=math.sqrt(25)
print(x)
x=math.sqrt(12)
print(x)
# floor give least value
#ceil give highest value

a=3.1
print(math.ceil(a)) 
print(math.floor(a))

# we can find sin cos and value of all the angles 
print(math.sin(0))
print(math.cos(0))

#pow function to find power
print(3**3)
print(math.pow(2,3))

#print value of known constants
print(math.pi)
print(math.e)

# if i don't want to write math functions  then i can replace it also with any variable
import math as m 
print(m.pi)

#if we want specific functions from math and we don't want to write math or any variable
from math import sqrt,pow
print(pow(2,3))
print(m.exp(2))

 
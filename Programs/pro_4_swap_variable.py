#swappin with using third variable
a=2
b=3
print(a,b)
temp=a
a=b
b=temp
print(a,b)
#swapping without using third variable 
a=a+b
b=a-b
a=a-b
print(a,b)
#SWAPPING IN PYTHON
a,b=b,a
print(a,b)
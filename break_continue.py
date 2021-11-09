"""
x=int(input("How many candies u want "))
i=1
av=5
while i<=x: # i<=5 1,2,3,4,5
    if i>av: # 1>5 , 2,3,4,5, 6>5
        print("out of stock")
        break
    print('candy')
    i+=1
print("end ")

x= float((input("How many candies u want ")))
a=5
for i in x:
    if i>a: 
        print("out of stock")
        break
    print('candy')
    i+=1
print("end ")    ---------> int, float  is not iterable 
av=5
for i in range(1,10):
    if i>av:
        print("out of stock ")
        break
    print("candy ")
 
#CONTINUE 
for i in range(1,101):
    if i%3==0 and i%5==0:  # it will skip only those which are divisible by both 
        continue 
    print(i,end=" ")
"""
# 1. don't want to print odd no.
for i in range(1,101):
    if i%2==0:
        pass
    else:
        print(i,end=" ")
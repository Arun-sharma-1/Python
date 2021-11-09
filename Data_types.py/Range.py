print(range(100))
print(list(range(100)))
# print(tuple(range(100)))
# print(set(range(100)))
print('EVEN NO LIST ')
print(list(range(0,102,2)))

#GET INDEX OF ELEMENT IN THE LIST 
A=range(1,10)
print(A)
print(A.index(3))

#GET VALUE AT ANY INDEX 
print(A[3])

# sevens=range(7,1000,7)
# n=int(input("Enter a no to check that it is divisible by seven or not "))
# if n in sevens:
#     print("{} is divsible by 7".format(n))

#HOW TO ADD DIFFERENCE IN RANGE 
A=range(1,10)
A=A[::2]
print(A)

#COMPARING TWO RANGES
print(range(0,5,2)==range(0,6,2)) 
# Reason --> [0,2,4 ]=[0,2,4]
print(range(0,100)[::-2]==range(99,0,-2))


#PRINTING RANGE IN REVERSE ORDER 
# r=range(0,100)
# for i in r[::-2]:
#     print(i)
# print("-" *20)
# for i in range(99,0,-2):
#     print(i)

#PRINTING REVERSE STRING 
back="AMRAHS NURA"
print(back[::-1])

#EXPERIMENT 
o=range(0,100,4)
print(o)
p=o[::5]
print(p)
for i in p:
    print(i)

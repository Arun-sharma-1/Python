for i in range(1,13):
    print(" {0:2} square is {1:4} and cube is {2:4}".format(i,i**2,i**3)) # right aligned 
print()
for i in range(1,13):
    print(" {0:2} square is {1:<4} and cube is {2:<4}".format(i,i**2,i**3))  #left aligned
print()
for i in range(1,13):
    print(" {0:2} square is {1:^4} and cube is {2:^4}".format(i,i**2,i**3))  #center aligned
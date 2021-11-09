

"""
X=[12,13,14,15,116]
for i in X:
    # print(X)
    print(i,end=" ")
print( )
for j in [1,2,3,4,5]:
    print(j,end=" ")
    print( )

for k in range(11,21,2): # 2 means difference betweeen value is 2 
    print(k,end=" ")
 
x=5
for i in x:
    print(i)
#an int object is not iterable and so is a float object. The integer object number is not iterable, 
# as we are not able to loop over it.
# """

y='arun'
for i in y:
    print(i)

for i in range(12,7,-2):
    print(" value  become {0:^5} " .format(i))

for i in range(12,2):
    print(i)             # NO ERROR+NO OUTPUT 

for i in range(1, 12//4): # range(1,12/4) this will give an error coz 12/4 is float and 1 is int 
    print(i)
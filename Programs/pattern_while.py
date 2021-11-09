####
####
####
####
####
"""
i=1
while i<=4:
    print("#",end="")
    j=1
    while j<=3:
        print("#",end="")
        j=j+1
    i=i+1
    print( )
 
for i in range(4):  # i is row , j is colomn
    for j in range(4):
         print("#",end=" ")
    print( )

#
# #
# # #
# # # #
for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print( )

    ####
    ###
    ##
    #
print("\n")
n=4
for i in range(n):
    for j in range(4-i):
        print("#",end=" ")
    print()
    
    """
  
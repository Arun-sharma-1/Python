"""
i=1
while i<6:
    print("Hello Alien's", i)
    i+=1
    # i++ Python, by design, does not allow the use of the ++ “operator”

j=5
while j>1:
    print("By Alien's")
    j=j-1
     
    #NESTING OF WHILE LOOP
i=1
# j=1
while i<=5:
    print('Arun ',end=" ")
    j=1
    while j<=5:
        print("sharma",end=" ")
        j=j+1
    i=i+1
    print( )
"""
direction_exit=["east", "west ","north", "south "]
to_found=""
while to_found not in direction_exit:  #not is used here because to_found conatain empty string  which is not present in list  
    to_found=input("choose dirction ")
    
print("you got it ")
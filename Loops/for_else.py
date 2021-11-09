numbers=[1,2,3,4,5,6,7,8]
for number in numbers:
    if number%8==0: # %8!=0 
        print("this is unexpected ")
        break
    # print('here')
 
else:
    print("now its fine ")

 
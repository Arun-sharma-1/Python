# write a code to print all the value form 1 to 100 skip the numbers which are divisible by 3 and 5
 
i = 1
while i <=100:
       # if not ((i%3 and i%5)!=0):
       if ((i%3 and i%5)!=0):
              print(i,end=" ")
       i =i +1


for i in range(1,101,1):
       if i%5!=0:
              print(i)
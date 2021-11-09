# n=int(input("Enter a no to find no of digit "))
# count=0
# while n:
#     no=n%10 # no=4
#     count+=1
#     n=n//10 # 1234 =123
# print(count)
 

i=1
while i<=100:
    if(i%3!=0 and i%5!=0 ):
        print(i,end=" ")
    i=i+1;
    
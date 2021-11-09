# n=int(input("Enter a no to find its sum "))
# sum=0
# while n:
#     no=n%10
#     sum=sum+no
#     n=n//10
# print(sum)

def sum(x):
    sum = 0;
    while x:
        temp = x % 10;
        sum = sum+temp;
        x = x//10
    print(sum)

sum(12 )

# n=int(input("Enter a number to Reverse "))
# rev=0
# while n:
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10 # n=n/10 this will not work 
# print(rev)
def reverse(x):
    rev=0
    while x: 
        temp=x%10  
        rev=rev*10 + temp  
        x=x//10 # n=floor(n/10)
    print(rev)

reverse(2234)

#using string slices
print(str(1235)[::-1])
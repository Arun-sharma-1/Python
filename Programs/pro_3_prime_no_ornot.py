# num=12111
# for i in range(2,num):
#     if num%i==0:
#         print('Not prime number ')
#         break
# else:
#     print("prime no ")

# x=12111
# for i in range(2,x):
#     if x%i==0:
#         print(i)

#prime no or not 
def prime_no():
    x=int(input())
    for i in range(2,x):
        if x%i==0:
            print('{} is not a prime no '.format(x))
            break;
    else:
        print("{} a prime no ".format(x))

prime_no()
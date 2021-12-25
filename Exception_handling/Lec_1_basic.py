def div(a, b):
    return a/b;


# a=int(input())
# b=int(input())
# try:
#     print(div(a,b))
# except:
#     print('error')

# try:
#     # print(10/0)
#     a = int('arun')
# except ZeroDivisionError:
#     print('You are trying to divide Number by 0')
# except:
#     print('Some error occured ')

# try:
#     # print(10/0)
#     a=int('arun')
# except Exception as e:
#     print(e)

# try:
#     raise Exception('Error created ')
# except Exception as e:
#     print(e)

class MyException(Exception): #this Exception word is required
    def __init__(self,msg) -> None:
        self.message = msg

try:
    raise MyException('Error created ')
except Exception as e:
    print(e)

# else will always execute if try dosen't throw any error
# finally will always execute
try:
    print('hello world ')
except:
    print('here error occured ')
else:
    print('middle world ')

finally:
    print('Tata world! ')

def func():
    try:
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4
print(func())
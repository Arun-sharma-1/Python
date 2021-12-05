#DEFAULT ARGUMENT
def add(data_1, data_2 , data_3=0):
    return data_1 + data_2 +data_3

result1=add(2,3,3)
result2=add(1,3)
result3=add(data_2=4,data_1=9) #KEYWORD ARGUEMENT
# print(result1 ,result2 ,result3)


#VARIABLE LENGTH ARGUMENT
def add(*n):
    total = 0
    for i in n:
        total+=i 
    print('Total is : ',total)
    print('tuple is :' , n)
   
add()
add(10)
add(10,20)
add(10,30)
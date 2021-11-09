from array import *
arr=array('i',[])
n=int(input("Enter the size of array "))
for i in range(n):
    x=int(input('Enter the value '))
    arr.append(x)
for i in range(n):
    print(arr[i],end=" ")
    print( )
search=int(input("Enter the value for search "))
k=0
for value in arr: # value is coming from not it is not like i 
    if value==search:
        print(k)
        break
    k=k+1
   
# WITH INBUILT FUNCTINS
print(arr.index(search))

# 1) Create an array with 5 values & delete the value at index no. 2 without using in-built function. 
# 2) write a code to reverse an array without using in-built function.
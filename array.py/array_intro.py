# #we can increase the size of array and we can also shrink it in python
# from array import *
# # import array
# val= array('i',[1,2,-3,4,5,8])
# # print(val)
# for i in range(6):
#     print(val[i]*val[i],end=" ")
# print( )
# i=0
# while i<6:
#     print(val[i],end=" ")
#     i+=1
# val.reverse()
# print(val)
# print(val[1])
# print(val.buffer_info()) # address, size 
# print(len(val))

# v=array('I',[1,2,-3,4,5])  # only for +ve no 
# print(v)
from array import *
a=array('i',[1,2,3,3,2,1])
# y=12
a.append(12)
print(a)
a.pop(1) # pop takes index to remove element 
print(a)
a.sort()
print(a)


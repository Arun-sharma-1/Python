import numpy as np
import random

from numpy.lib.index_tricks import AxisConcatenator
# DEFINE ARRAY
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1], [11], [111], [1111]])
# print(a)
# print(type(a))
# print(b[0][0])

# SHAPE OF ARRAY = DIMENSIONS OF ARRAY
# print(a.shape)
# print(b.shape)

# CREATE ZEROS , ONES ,CUSTOM ARRAY
zero_matrix= np.zeros(3)
b = np.ones((3, 3))
# print(b)
# print(zero_matrix)


#ARRAY OF SOME CONSTANTS 
c= np.full((3,2),'*')
# print(c)

#IDENTITY MATRIX
d= np.eye(4)
# print(d)

#RANDOM MATRIX
random_matirx = np.random.random((2,3)) #different output in random.randint
# print(random_matirx)

#printing middle element in both col
# print(random_matirx[ :, 1])

#UPDATING VALUE OF RANDOM MATRIX
random_matirx[1, 1:2]=1
# print(random_matirx)

zero = np.zeros((3,2) ,dtype=np.int64)
# print(zero)
zero[0 , :]=5
zero[2 , 1:2] =7
print(zero)

#DATA TYPE 
# print(zero.dtype)
# print(d.dtype)
# # print(zero_matrix.dtype)

#RESHAPE ARRAY MATRIX
reshaped_zero=zero.reshape((2,3))
print(reshaped_zero)

print(' ')
#MATHEMATICAL OPERATIONS 
x = np.array([ [ 1,2 ] ,[ 3,4]])
y =np.array([ [ 1,2 ] ,[ 3,4]])
print(x+y) #element wise addition
print(np.add(x,y)) #both are same 

# print(x*y)
# print(np.multiply(x,y))

print(' ')
# print(np.sqrt(x))

#MATRIX MULTIPLICATION / DOT PROUCT
# print(x.dot(y))
# print(np.dot(x,y))

#MORE BASIC OPERATIONS

num = [2,3,4]
# print(sum(num))

num = np.array([ [ 1,2] ,[3,4]])
print(np.sum(num))
print(np.sum(num ,axis=1))

#STACKING OF ARRAY
A= np.array([1,2,3,4])
B=np.array([4,3,2,1])
B=B**2
print(B)

#concatenation of array
print(np.stack((A,B),axis=1))

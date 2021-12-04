import numpy as np

a = np.array([[1, 3, 4, 5], [3, 2, 42, -1]])
print(np.min(a,axis=1)) #np.min(a) #np.min(a,axis=0)

#AVERAGE
len = np.size(a)
sum = np.sum(a)
avg = sum/len 
print(avg)

avg = np.average(a)
avg_ = np.mean(a,axis=1)
print(avg_)
print(avg)

#MEDIAN
print(np.median(a))

#Statistical functions
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.amin(a,axis=1))
print(np.amax(a,axis=1))
print(np.amin(a,axis=0))
print(np.amax(a,axis=1))
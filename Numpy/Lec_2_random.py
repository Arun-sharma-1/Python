import numpy as np
from numpy import random
import random

# a=np.arange(10)
a= np.arange(10) +5
print(a)
np.random.shuffle(a)
print(a)

b= np.random.rand(2,3) 
c= np.random.randn(2,3)
d= np.random.randint(5,10,3) #give 3 no between 5 and 10
e= np.random.choice([3,4,62,4])
print(d)



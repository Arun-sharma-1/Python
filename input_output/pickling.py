from pickle import *
import pickle
names=(
    'arun',
    'kushal',
    ('rahul','yashwant',('meera','manoj'))
)
even=list(range(0,10,2))
odd=list(range(1,10,2))
with open('z6.txt','bw') as n:
    pickle.dump(names,n)
    pickle.dump(even,n)
    pickle.dump(odd,n,protocol=pickle.DEFAULT_PROTOCOL)


with open('z6.txt','rb') as naming:
    i=pickle.load(naming)
    j=pickle.load(naming)
    k=pickle.load(naming)
print(i)
print(j)
print(k)
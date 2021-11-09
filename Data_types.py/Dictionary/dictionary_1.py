#FORMAT OF DICIONARY
data={1:'arun', 2:'sharma',4:'its me '}
print(data)
print(data.get(2))

#ACCESS ELEMENT THROUGH KEY 
#print(data[x])--> x is the key which is present in dictionary 
print(data[4])

#IF KEY IS NOT PRESENT THEN IT WILL THROW AN ERROR 
# print(data[3]) -->error

#IF KEY IS NOT PRESENT THEN .get() WILL NOT GIVE ANY ERROR 
a=data.get(3) # it will not give any error
print(a)

#########
b=data.get(1,'Not found')  # value is already present at key 1 then it will not change the value 
print(b)
c=data.get(3,'Not Found')
print(c)
print('\n')


#MERGE TWO LISTS 
l1=[1,2,3]
l2=['arun','kumar','kushal']
d= dict(zip(l1,l2)) # case sensitive in context of brackets 
print(d)


#ADDING LIST IN THIS DICTIONARY 
d[4]='lavish'
print(d)
del d[2]
print(d)
print(d.keys())
print(d.values())

#DELETE FULL DICTIONARY WITH CLEAR 
d.clear()

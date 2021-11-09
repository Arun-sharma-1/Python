# In Python, strings are made immutable so that programmers cannot alter the contents of the object (even by mistake). This avoids unnecessary bugs.
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

name='arun'
for char in name:
    print(char)

#FIND INDEX OF ANY ELEMENT IN STRING
print(name.find('b'))
#if element is not present then it will return -1

name='arun sharma'
# print(name[:])
# print(name[::-1])
# print(name[5:4:-1])
#string functions
print(name.find('a')) # return index of  first a
print(name.rfind('a')) #return index of last a
print(name.split()) #default value of split is space 
print(name.split('a'))#default value changed to a and a will lost
print(name.index(' ')) #return index of space 
print(name.capitalize)#No error it will give information about these functions if we don't use bracket
print(name.lower)
print(name.lower())
print(name.upper())
print(name.capitalize()) # only capitalize first characther

print(name.casefold()) # work same as lower
print('-'*20)

print(name.endswith('n'))
print(name.isdigit())
print(name.islower())
print(name.isupper())
print(name.count('a'))
print(name.isspace())
print(name.isalpha())
print(name.isalnum())
print(name.strip()) #remove space
print(name.swapcase())
print(name.replace('a','s')) #replace all a with s
print(print(name))
print(name.center(100))
print(name.isidentifier())

rllno='12'
print(rllno.zfill(12)) 


print(name.join('as'))
print('arun sharma'.join('as as'))
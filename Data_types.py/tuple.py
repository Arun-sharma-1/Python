# () these brakets told us about tuple
s=(22,25,14,21,5)
print(s)
print(s[3])  
# tuple is not mutable u cannot change the value 

#DIFFERENCE BETWEEN TUPLE AND STRING 
atuple=("orange")
print(type(atuple))

atuple=("orange",)
print(type(atuple))

########
t="a","b",1
print(t)
print(t[0])
print(type(t))
########
ti="a",
print(type(ti))

#CHANGE VALUE OF TUPLE 
name=("arun","sharma",2001)
# name[1]="kumar"               error we can not change value of tuple like this 
name=name[0],"kumar ",name[2]
print(name)
name="kushal",name[1],name[2]
print(name)

##########
name=("arun","sharma",2001)
a,b,c=name
print(a)
print(b)
print(c)

#####
# name=("arun","sharma",2001)
# a,b=name
# print(a)
# print(b)   THIS IS AN ERROR


#########
fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
mytuple = fruits * 2
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

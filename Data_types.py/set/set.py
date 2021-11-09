# {} these brackets tell us about set 
#1st WAY TO CREATE SET 
s={22,25,14,21,5}
print(s)
for i in s:
    print(i)

#2nd WAY TO CREATE SET 
s1=set([12,13,14])
print(s1)
for i in s1:
    print(i)

# ADD ELEMENT IN SET
s.add(121)
print(s)

#CREATE EMPTY SET 
empty={} #THIS IS DICTIONARY NOT SET 
print(type(empty))

empty_set=set()
print(type(empty_set))

# TUPLE TO SET 
tuple=(11,12,13,14)
print(set(tuple))
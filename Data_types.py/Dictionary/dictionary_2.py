#DICTIONARY WITH FOR LOOP

# for i in fruit:
#     print(i +" is " + fruit[i])
fruit={ "lemon":"citrus, not good in taste ",
        "orange":"good in taste and orange in color ",
        "apple":"red in colour",
        "banana":"good for increasing weight "}

#EACH TIME ORDER MAY BE DIFERENT
# for i in range(10):
#     for snacks in fruit:
#         print(snacks + " is "+fruit[snacks])
#     print("= " *30)

#ORDERED DICTIONARY
ordered_keys=list(fruit.keys())
ordered_keys.sort()
# or --> ordered_keys=sorted(list(fruit.keys()))

for f in ordered_keys:
    print(f + " - " + fruit[f])
print()
 
#######
# for f in sorted(fruit.keys())
#       print(fruit[f])

########
for key in fruit:
    print(fruit[key])
print()

#ADD MORE ITEMS TO DICTIONARY
fruit["tomato"]="very tasty"
for key in fruit:
    print(fruit[key])
print()

####
print(fruit.items())

#MAKING TUPLE USING DICITONARY
f_tuple=tuple(fruit.items())
print(f_tuple)

for snaks in f_tuple:
    print(snaks)

#TUPLE TO DICTIONARY 
print(dict(f_tuple))
 
#CHANGING VALUE OF DICTIONARY WITH OTHER DICITONARY
fruit={ 1:"orange",
        2:"apple",
        3:"banana"
       
}
print(fruit)

laptop={ 1:"Acer ",2:" dell",3:"lenovo" }
print(laptop)

# laptop.update(fruit)
# print(laptop)
# print(laptop.update(fruit))  this is not right syntax it will give None 


#COPY VALUE OF ONE DICTIONARY TO ANOTHER 
a=fruit.copy()
a.update(laptop)
print(a)

#CREATE EMPTY DICTIONARY
empty={} #THIS IS  EMPTY DICTIONARY  
print(type(empty))


####
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
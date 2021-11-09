# #UNION
# even=set(range(0,40,2))
# print(even)

# sq_tuple=(1,4,9,16)
# square=set(sq_tuple)
# print(square)

# print(even.union(square))
# print(square.union(even))

# #INTERSECTION
# print(even.intersection(square))
# print(even & square)
# # print(square.intersection(even))
# # print(square & even)

#DIFFERENCE
even=set(range(0,40,2))
print(sorted(even))

sq_tuple=(1,4,9,16,25)
square=set(sq_tuple)
print(sorted(square))

print(sorted(even.difference(square)))
# print(sorted(even-square))
print(sorted(square.difference(even)))
# print(sorted(square-even))

# a={1,2,3,4}
# b={1,2,3}
# print(sorted(a.difference(b)))
# # print(sorted(a-b))
# print(sorted(b.difference(a)))


# #SYMMETRIC DIFFERENCE 
# print(sorted(a.symmetric_difference(b)))
# print(even.symmetric_difference(square))

# #DISCARD 
# a.discard(4)
# a.remove(3)
# a.discard(34)  #NO error, do nothing 
# # a.remove(34) THIS WILL GIVE ERROR 
# #IF WE DON'T WANT ERROR 
# if 34 in a:
#     a.remove(34)
# print(a)
# a.add(3)
# print(a)
# print( )

# #SUBSET AND SUPERSET 
# a={1,2,3,4,5}
# b={1,2,3,4}
# if a.issuperset(b):
#     print("A is superset of B ")
# if b.issubset(a):
#     print("B is subset of A")

# #FROZEN SET -->IMMUTABLE
# a=frozenset(1,2,3,4)
# # a.add(2) -->error 
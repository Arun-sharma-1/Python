L=["egg", "fish","vegetables","milk","pens"]
 
# for i in range(1,5 ):   
#     print(L[i])
item_to_find="milk"
found_at=None
# if 6 line is not present and item is not present in list then it will show error 
for i in range(len(L)):
    if L[i]==item_to_find:
        found_at=i
        break

print("item found at {0} index ".format(found_at))

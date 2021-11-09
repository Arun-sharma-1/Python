data=input("Enter string with special characthers ")

# for char in data:
#     if not char.isalpha() and char.isnumeric():
#         char.replace(char,'')
# print(char)


new_data=''
for char in data:
    if  not char.isalnum():
        continue;
    else:
        new_data+=char

print(new_data)




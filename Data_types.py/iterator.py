# string="12345678"
# my_iterator=iter(string)
# print(my_iterator)
# print(next(my_iterator))
# while len(string):
#     print(next(my_iterator))
#     pass
 
string="12345678"
for char in string:
    print(char)
print()
for char in iter(string):
    print(char)
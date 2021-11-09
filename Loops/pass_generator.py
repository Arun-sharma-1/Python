#EASY - VERSION
import random

print('Welcome to password Generator!')

list_letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
length_letter=len(list_letter)
list_number=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_symbol=['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters=int(input('How many letters would you like in your password '))
symbol=int(input("How many symbol would you like "))
number=int(input("How many Numbers would you like "))

passw=" ";

for i in range(1,letters+1):
    random_char=random.choice(list_letter) #string type
    # print(random_char,end="")
    passw+=random_char;
    

 
for i in range(1,symbol+1):
    random_sy=random.choice(list_symbol)
    # print(random_sy,end="")
    passw+=random_sy


for i in range(1,number+1):
    random_no=random.choice(list_number)
    # print(random_no,end="")
    passw+=random_no
# print(passw)

#HARD-VERSION
passE=[]

for i in range(1,letters+1):
    random_char=random.choice(list_letter) #string type
    # print(random_char,end="")
    passE+=random_char;
    

 
for i in range(1,symbol+1):
    random_sy=random.choice(list_symbol)
    # print(random_sy,end="")
    passE+=random_sy


for i in range(1,number+1):
    random_no=random.choice(list_number)
    # print(random_no,end="")
    passE+=random_no
print(passE)
random.shuffle(passE);
# print(str(passE))
str1=''.join(passE)
print(str1)

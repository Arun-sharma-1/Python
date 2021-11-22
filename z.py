# d1={1:'arun' , 2:'kusahl'};
# d2={3:"ram",4:'ravan'};
# d ={}
# for i in d1,d2:
#     d.update(i)
# print(d)
# import random;
# list=['ardvark','baboon','camel']
# choosen_word=random.choice(list)
# print(f'choosen word is {choosen_word}')


# display=[];
# for i in range(len(choosen_word)):
#     display+='_'

# print(display)

# list=['a','b','a']
# print(list. index('a'))
# new_letter=alphabelt[new_position]

# enemy = 1
# def fn():
#     global enemy
#     enemy+=1
#     return enemy
# print(fn())
# import tkinter

# root = tkinter.Tk()
# root.mainloop()
import sqlite3
db = sqlite3.connect('contacts.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS contacts (name TEXT , phone integer)')
db.execute('INSERT INTO contacts VALUES("Arun" , 111) ')
db.execute('INSERT INTO contacts VALUES("SOMEONE" , 222) ')


cursor  = db.cursor()
cursor.execute('select * from contacts')
for name ,phone in cursor:
    print(name)
    print(phone)
    print('-'*20)
cursor.close()
# db.execute('drop table contacts')

db.close()

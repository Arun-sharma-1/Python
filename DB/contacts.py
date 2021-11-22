import sqlite3
db = sqlite3.connect('contacts.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS contacts (name TEXT , phone integer)')
db.execute('INSERT INTO contacts VALUES("Arun" , 111) ')
db.execute('INSERT INTO contacts VALUES("SOMEONE" , 222) ')

cursor  = db.cursor()
cursor.execute('select * from contacts')
# for row in cursor:
#     print(row)

# print(cursor.fetchall()) #Return list 

# print(cursor.fetchone()) #returns one by one item
# print(cursor.fetchone())
# print(cursor.fetchone()) #if item is not present then it will show None

#IF you print this for loop two times it will give output only 1 time 
for name ,phone in cursor:
    print(name)
    print(phone)
    print('-'*20)

        #EVERYTIME IT CREATE NEW ONE IF WE EXECUTE THIS COMMAND 
# for name, phone in db.execute('SELECT * FROM contacts'):
#     print(name)
#     print(phone)
#     print('-'*20)

# db.execute('drop table contacts')
cursor.close()
db.commit() #if we do commit then data saved permanently in the file and everytime we get duplicate data
db.close()


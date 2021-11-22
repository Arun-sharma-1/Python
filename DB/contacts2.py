import sqlite3
from sqlite3.dbapi2 import Cursor
db = sqlite3.connect('contacts.sqlite')

# UPDATE
no = input('Enter number : ') #string
# update_sql = "update contacts set phone={} where contacts.name='Arun' ".format(no)
update_sql = "update contacts set name='Arunsharma' where contacts.phone={} ".format(no)
update_cursor =db.cursor();
update_cursor.execute(update_sql)
print("{} rows updated ".format(update_cursor.rowcount))
update_cursor.connection.commit()

# first commit contacts then we can use this method
# for name, phone in db.execute('SELECT * FROM contacts'):
#     print(name)
#     print(phone)
#     print('-'*20)

update_cursor.execute('select * from contacts')
for name , phone in update_cursor:
    print(name)
    print(phone)

update_cursor.close()
db.close()

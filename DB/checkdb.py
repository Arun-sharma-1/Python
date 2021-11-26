from os import name
import sqlite3

conn = sqlite3.connect('contacts.sqlite')

# for row in conn.execute("select * from sqlite_master"):
#     print(row)
name=input('Enter ur name : ')
# for row in conn.execute("select * from contacts where name = ?",(name,)): #tuple method for input
#     print(row)

for row in conn.execute("select * from contacts where name LIKE ?",(name,)): #like removes the case sensitiveness
    print(row)
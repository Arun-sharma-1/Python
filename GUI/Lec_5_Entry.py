from tkinter import *
from typing import Collection
root = Tk()
root.geometry('500x400')
root.title('Entry')

user = Label(root, text='Username : ')
passw = Label(root, text='password : ')

user.grid(row=0, column=0)
passw.grid(row=1, column=0)

#Variable class in Tkinter
# BooleanVar ,DoubleVar , IntVar , StringVar 

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=IntVar)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

root.mainloop()

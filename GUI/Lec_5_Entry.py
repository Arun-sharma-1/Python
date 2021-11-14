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

def submit():
    print(no.get())
uservalue = StringVar()
passvalue = StringVar()

no =StringVar() #if we use intvar() then by default it is giving 0
userentry = Entry(root, textvariable=no)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

btn=Button(root,text='Submit this form',command=submit)
btn.grid(row=2,column=1)

root.mainloop()

from tkinter import *
from typing import Collection
root = Tk()
root.geometry('500x400')
root.title('Events')
def arun(event):
    print(f'You clicked on the button at {event.x} ,{event.y}')
# widget  = Button(root, text='click on this ')
# widget.pack()

# widget.bind('<Button-1>',arun)
# widget.bind('<Double-1>',quit) #Exit on double click
# root.mainloop(


#PROGRAM TO CHANGE WIDTH OF GUI
def size():
    a=height.get()
    b=width.get()
    print(height.get())
    print(width.get())
    root.geometry(f'{a}x{b}')
     
lable_1 = Label(text='Enter height: ')
lable_2 = Label(text='Enter width: ')
lable_1.grid(row=0 ,column=0,padx=10,pady=10)
lable_2.grid(row=1,column=0,padx=10,pady=10)

width=StringVar()
entry_1 = Entry(root, textvariable=width)

height = StringVar()
entry_2 = Entry(root, textvariable=height)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

btn = Button(text='Change Size ',bg='lightgreen',command=size)
btn.grid(row=3,columnspan=2,padx=20,pady=10)

root.mainloop()


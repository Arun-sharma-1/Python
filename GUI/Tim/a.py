from tkinter import *
from typing import Collection
root = Tk()
root.geometry('640x480')
root.title('a')
label = Label(root, text='arun sharma')
label.grid(row=0 ,column=0)

left_frame = Frame(root,bg='green',relief=RAISED,borderwidth=1 ,height=30 )
left_frame.grid(row=1 ,column=1)

Can = Canvas(left_frame,relief=RAISED , borderwidth=1)
Can.grid(row=1 ,column=1)

right_frame = Frame(root,relief=RAISED,borderwidth=1 ,height=30 )
right_frame.grid(row=1 ,column=2 ,sticky='n')

btn_1 = Button(right_frame ,text='btn-1')
btn_2 = Button(right_frame ,text='btn-2')
btn_3 = Button(right_frame ,text='btn-3')

btn_1.grid(row=0,column=0)
btn_2.grid(row=1 ,column=0)
btn_3.grid(row=2,column=0)

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)

right_frame.grid(sticky='new')
right_frame.config(relief=SUNKEN,borderwidth=1)

right_frame.columnconfigure(0,weight=1)

btn_2.grid(sticky='ew')
root.mainloop()
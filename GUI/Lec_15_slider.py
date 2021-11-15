from tkinter import *
from tkinter import messagebox as msg
from typing import Collection, ValuesView
root = Tk()
root.geometry('500x400')
root.title('Slider')
def amount():
    money=f'Amount to be transfered is {slider_1.get()}'
    msg.showinfo('amount', money)

label = Label(root, text='Enter the amount to be transferred ')
label.grid(row=0, column=0)
entry = Entry(root)

slider_1 = Scale(root,from_ =0,to=100 ,orient=HORIZONTAL,tickinterval=20,width=30)
slider_1.grid(row=1,column=0)
# slider_1.set(30)
btn = Button(text='click here to transfer money',command=amount)
btn.grid(row=1,column=1,pady=10)

root.mainloop()

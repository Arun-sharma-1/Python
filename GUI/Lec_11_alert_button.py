# from tkinter import *
from tkinter import messagebox

# root=Tk()
# root.geometry("500x500")

# def msg():
#     messagebox.showinfo("Message Window","Restart Your System")

# b1=Button(root,text="Hello World",bg="blue",fg="white",command=msg)
# #b1.pack()
# b1.place(x=60,y=100)

# root.mainloop()

from tkinter import *
root=Tk()

def msg(x):
    if x==1:
        messagebox.showinfo("Message Window","restart you system")
    elif x==2:
        messagebox.showinfo("Message Window","second message for your system")
    else:
        messagebox.showinfo("Message Window","it's the third message")
#msg()


b1=Button(root,text="Hello World",bg="red",fg="white",command=msg(1))
b1.pack()

b2=Button(root,text="Hello World",bg="red",fg="white",command=msg(2))
b2.pack()
b3=Button(root,text="Hello World",bg="red",fg="white",command=msg(3))
b3.pack()

root.mainloop()
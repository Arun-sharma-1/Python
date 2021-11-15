from tkinter import *
from typing import Collection
import tkinter.messagebox as msg
root = Tk()
root.geometry('500x400')
root.title('Menu and sub menu')
def myfunc():
    print("Thi is menu bar")
def help():
    print('Restart your program')
    a=msg.showinfo('help','Arun will make you out from this ')
#NON DROP DOWN MENU
# mymenu = Menu(root);
# mymenu.add_command(label='File',command=myfunc)
# mymenu.add_command(label='Quit',command=quit)
# root.config(menu=mymenu)

mainmenu = Menu(root)#tearoff for extra line
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label='New file',command=myfunc)
m1.add_command(label='save',command=myfunc)
m1.add_separator()
m1.add_command(label='saved file',command=myfunc)
m1.add_command(label='Exit',command=quit)

 
m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label='Help',command=help)
mainmenu.add_cascade(label='File',menu=m1)
mainmenu.add_cascade(label='Help' ,menu=m2)
root.config(menu=mainmenu,padx=10,pady=5)
root.mainloop()
from tkinter import *
from PIL import Image ,ImageTk
import tkinter
from tkinter import font

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill = x, y ,both
# padx
# pady

#Define window
root = Tk()
root.title('Lables and pack ')
root.geometry('450x300')
# root.resizable(0,0)
root.config(bg='lightyellow')

#create widgets
label_1 = Label(text='This is first para')
label_1.pack(anchor='ne')

label_2 = Label(text='This is second para ',bg='lightgreen',font=('Arial',18 ,'bold') ,fg='white',borderwidth=2 ,relief=GROOVE)
label_2.pack(pady=10 ,anchor='ne' ,fill='x' ,side=BOTTOM ,padx=34) #ne ,nw , se

label_3 =tkinter.Label(root)
label_3.config(text='This is third para')
label_3.config(font=('cambria',20))
label_3.pack(pady=(10,0) ,ipadx=50 , ipady=10 ,expand=True) #10 = top , 0=bottom ,fill='y' than expand =true
label_3.place(x=50 ,y=500) # this will fix the position like posn:fixed

D = Label(text="Date:-07.06.2020", bg="black", fg="white", borderwidth=3, padx=5, pady=5, relief=SUNKEN)
D.place(x=1000, y=70)

 
root.mainloop()
 
 
  
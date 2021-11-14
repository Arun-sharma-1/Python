#Images
from tkinter import *
#define root
root = Tk()
root.geometry('400x400')
root.title('working with images ')
#property
photo = PhotoImage(file='download.png',height=50, width=100)
label = Label(root ,image=photo)
label.pack()

btn =Button(root, image=photo)
btn.pack()
root.mainloop()
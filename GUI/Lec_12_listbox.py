from tkinter import *
root = Tk()
root.geometry('100x90')
root.title('Listbox')
#listbox

lb = Listbox(root,width=100,height=90);
lb.insert(1,'arun');
lb.insert(2,'ram')
lb.insert(3,'ravan')
lb.insert(4,'ramesh')
lb.pack()
root.mainloop()
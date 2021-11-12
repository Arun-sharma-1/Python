from tkinter import *
from typing import Collection
root = Tk()
root.geometry('400x400')
root.title('Buttons and Grids ')


def Hello():
    print('This will will appear on clicking')

# BUTTONS
# frame = Frame(root)
# frame.grid(row=0 ,column=0)
# frame.pack()


b1 = Button(root, fg='red', text='click now', command=Hello)
b1.grid(row=0, column=0, padx=10, pady=10)  # do not apply b1.pack() after grid

b2 = Button(fg='blue', text='second button', activebackground='lightgreen')
b2.grid(row=0, column=1)

b2 = Button(fg='blue', text='large button',
            activebackground='white', bg='black')
b2.grid(row=1, column=0, columnspan=3, sticky='WE', padx=10)

test_1 = Button(text='test')
test_2 = Button(text='test')
test_3 = Button(text='test')
test_4 = Button(text='test')
test_5 = Button(text='test')
test_6 = Button(text='test')

test_1.grid(row=2, column=0, padx=5, pady=5)
test_2.grid(row=2, column=1, padx=5, pady=5, sticky='W')
test_3.grid(row=2, column=2, padx=5, pady=5)
test_4.grid(row=3, column=0, padx=5, pady=5)
test_5.grid(row=3, column=1, padx=5, pady=5, sticky='W')
test_6.grid(row=3, column=2, padx=5, pady=5)


root.mainloop()

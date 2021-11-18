from tkinter import *
import tkinter
root = Tk()
root.title('Calculator')
root.geometry('440x280-8-200')
root['padx'] = 10
keys = [
    [('C', 1), ('CE',1)],
    [('7', 1), ('8',1), ('9', 1), ('+', 1)],
    [('4', 1), ('5',1), ('6', 1), ('-', 1)],
    [('1', 1), ('2',1), ('3', 1), ('*', 1)],
    [('0', 1), ('=',1), ('/', 1)]

]
scvalue =StringVar()
scvalue.set('')
result = Entry(root ,textvariable=scvalue)
result.grid(row=0,column=0,sticky='nsew')

keypad = Frame(root)
keypad.grid(row=1,column=0,sticky='nsew')

def button_click(number):
    # result.insert(0,number)
    print(number)
    pass


row = 0
for keyrow in keys:
    col=0
    for key in keyrow:
        Button(keypad ,text=key[0] ,command= lambda: button_click(key[0])).grid(row=row ,column=col ,sticky=W+E ,ipadx=3 ,padx=3 ,pady=3)
        col+=key[1]
    row+=1

root.update()
root.minsize(keypad.winfo_width() + 20, result.winfo_height() + keypad.winfo_height())
root.mainloop()
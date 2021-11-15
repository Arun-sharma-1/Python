#simple calculator
from tkinter import *
from typing import Collection
#define root
root = Tk()
root.title('Calculator ')
root.iconbitmap('arun.ico')
root.geometry('403x325')
root.resizable(0,0)
#define widgets
label_1=Label(root,bg='lightgreen',height=4 ,width=80)
label_1.pack() 
label_2=Label(root,height=40,width=70,bg='yellow')
label_2.pack(side=LEFT,fill=BOTH,expand=True) 
label_2.pack_propagate(0)

def onclick():
     label = Label(Entry,text=number.get)
     print(label)

def click(event):
    global scvalue  
    text = event.widget.cget("text")
    print(type(text))
    if text == '=':
        pass
    elif text=='C':
        scvalue.set('')
        e.update()
    else:
        scvalue.set(scvalue.get()+text)
        e.update()
# defined buttons
number = IntVar()
b1=Button(label_2, text='1',padx=50,pady=20)
b2=Button(label_2, text='2',padx=50,pady=20)
b3=Button(label_2, text='3',padx=50,pady=20)
b4=Button(label_2, text='4',padx=50,pady=20)
b5=Button(label_2, text='5',padx=50,pady=20)
b6=Button(label_2, text='6',padx=50,pady=20)
b7=Button(label_2, text='7',padx=50,pady=20)
b8=Button(label_2, text='8',padx=50,pady=20)
b9=Button(label_2, text='9',padx=50,pady=20)
b0=Button(label_2, text='0',padx=50,pady=20)
#operations
op_1=Button(label_2,text='+',padx=20,pady=20)
op_2=Button(label_2,text='-',padx=20,pady=20)
op_3=Button(label_2,text='*',padx=20,pady=20)
op_4=Button(label_2,text='/',padx=20,pady=20)

#packing opertions
op_1.grid(row=0,column=3)
op_2.grid(row=1,column=3)
op_3.grid(row=2,column=3)

 
#pack these buttons
b1.grid(row=2 ,column=0)
b1.bind('<Button-1>',click)
b2.grid(row=2 ,column=1)
b2.bind('<Button-1>',click)
b3.grid(row=2 ,column=2)
b3.bind('<Button-1>',click)
b4.grid(row=1 ,column=0)
b4.bind('<Button-1>',click)
b5.grid(row=1,column=1)
b5.bind('<Button-1>',click)
b6.grid(row=1 ,column=2)
b6.bind('<Button-1>',click)
b7.grid(row=0 ,column=0)
b7.bind('<Button-1>',click)
b8.grid(row=0 ,column=1)
b8.bind('<Button-1>',click)
b9.grid(row=0 ,column=2)
b9.bind('<Button-1>',click)
b0.grid(row=3 ,column=1)
b0.bind('<Button-1>',click)

#INPUT FEILD
scvalue =StringVar()
scvalue.set('')
e = Entry(label_1, width=35, borderwidth=5 ,textvariable=scvalue)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10,ipadx=10,ipady=10)

root.mainloop()
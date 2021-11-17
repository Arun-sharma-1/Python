from tkinter import *
import os
from typing import Collection
root = Tk()
root.geometry('640x480')
root.title('Grid demo')
label = Label(root, text='Grid Demo')
label.grid(row=0 ,column=0 ,columnspan=3)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=3)
root.columnconfigure(3, weight=3)
root.columnconfigure(4, weight=3)

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=10)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=3)
root.rowconfigure(4,weight=3)

filelist = Listbox(root)
filelist.grid(row=1, column=0, columnspan=2 ,sticky='news',rowspan=2)
filelist.config(border=2,relief=SUNKEN)

scroll = Scrollbar(root, orient=VERTICAL ,command=filelist.yview)
scroll.grid(row=1,column=1 ,sticky='nse' ,rowspan=2)
# filelist['yscrollcommand'] = scroll.set 

for zone in os.listdir('/Windows/System32'):
    filelist.insert(END,zone)

#FRAME FOR RADIO BUTTON
radiofra  = LabelFrame(root, text='File details')
radiofra.grid(row=1,column=2 ,sticky='ne')

rbvalue = IntVar()
radio_1 =Radiobutton(radiofra ,text='option-1' ,variable=rbvalue ,value=1)
radio_2 =Radiobutton(radiofra ,text='option-2' ,variable=rbvalue ,value=2)
radio_3 =Radiobutton(radiofra ,text='option-3' ,variable=rbvalue ,value=3)

radio_1.grid(row=0 ,column=0 ,sticky='w')
radio_2.grid(row=1 ,column=0 ,sticky='w')
radio_3.grid(row=2 ,column=0 ,sticky='w')



root.mainloop()
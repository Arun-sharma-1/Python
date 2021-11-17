from tkinter import *
import os
from typing import Collection
root = Tk()
root.geometry('640x480')
root.title('Grid demo')
root.config(bg='lightgrey')
label = Label(root, text='Grid Demo')
label.grid(row=0, column=0, columnspan=3)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=3)
root.columnconfigure(3, weight=3)
root.columnconfigure(4, weight=3)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=10)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=3)
root.rowconfigure(4, weight=3)

filelist = Listbox(root)
filelist.grid(row=1, column=0, columnspan=2, sticky='news', rowspan=2, padx=10)
filelist.config(border=2, relief=SUNKEN)

scroll = Scrollbar(root, orient=VERTICAL, command=filelist.yview)
scroll.grid(row=1, column=1, sticky='nse', rowspan=2)
# filelist['yscrollcommand'] = scroll.set

for zone in os.listdir('/Windows/System32'):
    filelist.insert(END, zone)

# FRAME FOR RADIO BUTTON
radiofra = LabelFrame(root, text='File details', bg='lightgrey')
radiofra.grid(row=1, column=2, sticky='ne', ipadx=10, ipady=10)

rbvalue = IntVar()
radio_1 = Radiobutton(radiofra, text='option-1',
                      variable=rbvalue, value=1, bg='lightgrey')
radio_2 = Radiobutton(radiofra, text='option-2',
                      variable=rbvalue, value=2, bg='lightgrey')
radio_3 = Radiobutton(radiofra, text='option-3',
                      variable=rbvalue, value=3, bg='lightgrey')

radio_1.grid(row=0, column=0, sticky='w')
radio_2.grid(row=1, column=0, sticky='w')
radio_3.grid(row=2, column=0, sticky='w')

# RESULT PART
label = Label(root, text='Result ')
label.grid(row=2, column=2, sticky='nw', ipady=5, padx=5)

entry = Entry(root)
entry.grid(row=2, column=2, sticky='sw', padx=5)

# FRAME FOR TIME
tf = LabelFrame(root, text=' Time ', bg='lightgrey')
tf.grid(row=3, column=0, sticky='new', padx=10, pady=10, ipady=5, ipadx=10)

hourspinner = Spinbox(tf, width=3, values=tuple(range(0, 24)))
minutespinner = Spinbox(tf, width=3, from_=0, to=59)
secondspinner = Spinbox(tf, width=3, from_=0, to=59)

hourspinner.grid(row=0, column=0)
minutespinner.grid(row=0, column=2)
secondspinner.grid(row=0, column=4)
tf['padx'] = 36


# DATE SPINNER
dateframe = Frame(root, bg='lightgrey')
dateframe.grid(row=4, column=0, sticky='new', padx=10)
# DATE
daylabel = Label(dateframe, text='Day', bg='lightgrey')
monthlabel = Label(dateframe, text='month', bg='lightgrey')
yearlabel = Label(dateframe, text='Year ', bg='lightgrey')

daylabel.grid(row=0, column=0, sticky='w')
monthlabel.grid(row=0, column=1, sticky='w')
yearlabel.grid(row=0, column=2, sticky='w')
# SPINNERS
dayspinner = Spinbox(dateframe, width=6, from_=1, to=31)
monthspiner = Spinbox(dateframe, width=6, values=(
    'jan', 'feb', 'mar', 'april', 'may', 'june', 'july ', 'august', 'sept ', 'oct', 'nov', 'dec'))
yearspinner = Spinbox(dateframe, width=6, from_=2010, to=2030)

dayspinner.grid(row=1, column=0)
monthspiner.grid(row=1, column=1)
yearspinner.grid(row=1, column=2)
# BUTTONS
okbutton = Button(root, text='Ok ')
cancelbutton = Button(root, text='Cancel ', command=quit)

okbutton.grid(row=4,column=3 , sticky='w')
cancelbutton.grid(row=4,column=3 ,sticky='e')


root.mainloop()

from tkinter import *
root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Radio')

input_frame = LabelFrame(root, width=350, height=100, text="this is fun")

output_frame = Frame(root, width=350, height=100 ,bg='green')
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=1)
output_frame.propagate(0)

def printing_no():
    select = 'You selected for option '+ str(number.get())  
    label.config(text = select) #this is used so that we text does not repeat otherwise we can use label method to print 
    # label = Label(output_frame , text=number.get())
    # label.pack()
    

# CHECKBOX
number = IntVar()
radio_1 = Radiobutton(input_frame,text='print the first number ', variable=number,value=1)
radio_2 = Radiobutton(input_frame, text="print the second number ",variable=number, value=2)
print_button = Button(input_frame, text='Print the Number' ,command=printing_no)

radio_1.grid(row=0,column=0,padx=10,pady=10)
radio_2.grid(row=0, column=1,padx=10,pady=10)
print_button.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

label =Label(output_frame)
label.pack()
root.mainloop()

# def sel():
#    selection = "You selected the option " + str(var.get())
#    label.config(text = selection)
 
# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
#                   command=sel)
# R1.pack( anchor = W )

# R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
#                   command=sel)
# R2.pack( anchor = W )

# R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
#                   command=sel)
# R3.pack( anchor = W)

# label = Label(root)
# label.pack()
# root.mainloop()
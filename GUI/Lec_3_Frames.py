from tkinter import *
root =Tk()
root.title('Frames Basic')
root.geometry('400x400')
root.resizable(0,1)

# Define Frames 
# pack_frame_1 = Frame(bg='red')
# pack_frame_2 =Frame(bg='blue')
# pack_frame  =LabelFrame(text='This is label frame ')

# # pack_frame_1.pack(fill=BOTH ,expand=True ,width=500 , height =400)
# pack_frame_1.pack(fill=BOTH ,expand=True)
# pack_frame_2.pack(fill=BOTH ,expand=True)
# pack_frame.pack(fill=BOTH ,expand=True , padx=20 ,pady=20) #use fill or use width and height

# Label(pack_frame_1 ,text='this is the first text') .pack()

# Label(text='This is my next text ').pack(pady=40 ,expand=True) 

def input():
    # print(entry.get())
    text  = Label(output_frame, text=entry.get())
    text.pack()

    entry.delete(0,END) #for deleting the text inside the entry after clicking on it

# def count():
#     Count=1
#     text=Label(third_frame,ACTIVE,text=Count )
#     Count+=1
#     text.pack()

frame =Frame(root, bg='red',width=500,height=100 ,borderwidth=5)
frame.pack(padx=10 ,pady=10)
entry =Entry(frame ,width=40)
entry.grid(row=0,column=0,padx=10 ,pady=10)
frame.grid_propagate(0)
btn =Button(frame ,text='submit',command=input)
btn.grid(row=0, column=1)


output_frame =Frame(root,bg='lightgreen', width=400 ,height=100)
output_frame.pack(padx=10 ,pady=10)
output_frame.pack_propagate(0) #if text come at the place of bg

third_frame = Frame(root, bg='green',width=500,height=300,borderwidth=3 ,relief=GROOVE)
third_frame.pack(padx=10 ,pady=10 )

# btnn = Button(frame ,text='Count',command=count)
# btnn.grid(row=2,sticky="WE",columnspan=4,column=0)
 
root.mainloop()
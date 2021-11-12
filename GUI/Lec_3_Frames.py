from tkinter import *
root =Tk()
root.title('Frames Basic')
root.geometry('400x400')

#Define Frames 
pack_frame_1 = Frame(bg='red')
pack_frame_2 =Frame(bg='blue')
pack_frame  =LabelFrame(text='This is label frame ')

pack_frame_1.pack(fill=BOTH ,expand=True)
pack_frame_2.pack(fill=BOTH ,expand=True)
pack_frame.pack(fill=BOTH ,expand=True , padx=20 ,pady=20)

Label(pack_frame_1 ,text='this is the first text') .pack()

Label(text='This is my next text ').pack(pady=40 ,expand=True) 


root.mainloop()
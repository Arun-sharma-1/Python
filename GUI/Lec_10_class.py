# from tkinter import *
# root=Tk()

# mb=Menubutton(root,text="Flower",relief="raised")
# mb.pack()
# mb.menu=Menu(mb)
# mb["menu"]=mb.menu
# lilly=IntVar()
# rose=IntVar()
# mb.menu.add_checkbutton(label="Lilly",variable=lilly)
# mb.menu.add_checkbutton(label="Rose",variable=rose)
# mb.pack()
# root.mainloop()


# checkbox
# from tkinter import *
# root=Tk()
# def Tick():
#     label = Label(root, text=cvar1.get())#if ticket than show 1 othewise 0
#     label.pack() 
# cvar1=IntVar()
# cvar2=IntVar()
# cvar3=IntVar()
# c1=Checkbutton(root, text="Chandigarh",variable=cvar1)
# c1.pack()

# c2=Checkbutton(root, text="New Delhi",variable=cvar2)
# c2.pack()
# c3=Checkbutton(root, text="Banglore",variable=cvar3)
# c3.pack()

# btn =Button(root, text='check status',command=Tick)
# btn.pack()
# root.mainloop()

# from tkinter import *
# root=Tk()

# L1=Label(root,text="Username")
# L1.pack(side=LEFT)

# E1=Entry(root,fg="red")
# E1.pack(side=LEFT)
# root.mainloop()


#Button's relief styles
# from tkinter import *
# root=Tk()/

# b1=Button(root,text="FLAT",relief="flat")
# b2=Button(root,text="RAISED",relief="raised")
# b3=Button(root,text="SUNKEN",relief="sunken")
# b4=Button(root,text="GROOVE",relief="groove")
# b5=Button(root,text="RIDGE",relief="ridge")

# b1=Button(root,text="Error",relief="raised",bitmap="error")
# b2=Button(root,text="Information",relief="raised",bitmap="info")
# b3=Button(root,text="Warning",relief="raised",bitmap="warning")
# b4=Button(root,text="Question",relief="raised",bitmap="question")
# b5=Button(root,text="Hourglass",relief="raised",bitmap="hourglass")

# b1.pack()
# b2.pack()
# b3.pack()
# b4.pack()
# b5.pack()
# root.mainloop()

#bring image
# from tkinter import*
# root=Tk()
# c=Canvas(width=500,height=500,bg="grey")
# c.pack()
# img=PhotoImage(file="a.jpg")
# c.create_image(50,10,image=img)
# root.mainloop()


#button
from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("500x500")

def msg():
    messagebox.showinfo("Message Window","Restart Your System")

b1=Button(root,text="Hello World",bg="blue",fg="white",command=msg)
#b1.pack()
b1.place(x=60,y=100)
 

root.mainloop()
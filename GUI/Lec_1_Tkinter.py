from tkinter import *
from PIL import Image ,ImageTk


#define window 
root = Tk()
#GUI LOGIC
root.title('Window Basics')
root.geometry('600x600') #widthxheight
root.minsize(200,100) #width ,height
root.resizable(1,0)
root.iconbitmap('arun.ico')
root.config(bg='lightgreen')
# photo = PhotoImage(file='download.png')

#for jpg image
photo = Image.open("arun.jpg")
photo = ImageTk.PhotoImage(photo)
arun_label= Label(image=photo)
arun_label.pack()

#Second window
top = Toplevel()
top.title('second window')
top.geometry('200x200+500+100')
 
# image = Image.open("download.jpg")
# pic = ImageTk.PhotoImage(image)
# sher_label = Label(image = pic)
# sher_label.pack()

 

#LOOP
root.mainloop()
# root.title('Window Basics')  This will not work here title should be in logic part 

from tkinter import *
from typing import Collection
root = Tk()
root.title('Canvas')
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
my_canvas = Canvas(root, width=300 ,height=200 ,bg='green')
my_canvas.pack(pady=20)

# x1,y1,x2,y2
# my_canvas.create_line(0,100,300,100 ,fill='red')
# my_canvas.create_line(150,0,150,200,fill='red')
 
# my_canvas.create_rectangle(x1,y1,x2,y2)
# rectange x1,y1 :Top left 
# rectangle x2,y2 :Bottom right
# my_canvas.create_rectangle(50,150,250,50,fill='black')
# my_canvas.create_oval(50,150,250,50,fill='cyan') #same as rectangle

my_canvas.create_line(0 , 500 , 300 ,50)
root.mainloop()
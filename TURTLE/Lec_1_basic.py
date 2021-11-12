import turtle as t
# t.goto(-100 ,-100)
# # t.goto(-100 ,-10)
# t.goto(-100,-40)
t.Screen().exitonclick()

t.penup()
t.pendown()
t.forward(100)
t.pendown()

import turtle

col=('yellow','red','green','orange','blue','white')

t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(30)

for i in range (150):

    t.color(col[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(2)

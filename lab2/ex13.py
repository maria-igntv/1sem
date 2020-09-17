import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed('fast')

def half_curcle(a):
    n = 50
    for i in range (n//2):
        turtle.forward(a*2*(np.pi)/n)
        turtle.left(360/n)

def curcle(a):
    n = 50
    for i in range (n):
        turtle.forward(a*2*(np.pi)/n)
        turtle.left(360/n)


turtle.begin_fill()
curcle(90)
turtle.color('yellow')
turtle.end_fill()
turtle.color('blue')
turtle.penup()
turtle.goto(-45, 105)
turtle.begin_fill()
curcle(10)
turtle.end_fill()
turtle.goto(45, 105)
turtle.begin_fill()
curcle(10)
turtle.end_fill()
turtle.goto(5, 88)
turtle.pendown()
turtle.color('black')
turtle.left(270)
turtle.width(8)
turtle.forward(25)
turtle.penup()
turtle.goto(-40, 60)
turtle.pendown()
turtle.color('red')
half_curcle(45)

turtle.exitonclick()

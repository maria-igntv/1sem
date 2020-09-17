import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(0)

curcles = 10

turtle.left(90)
def curcle(i_c):
    n = 50
    a = 20*i_c
    for i in range (n):
        turtle.forward(a*2*(np.pi)/n)
        turtle.left(360/n)

for i_curcle in range(curcles):
    curcle(i_curcle)
    turtle.left(180)
    curcle(i_curcle)
    turtle.left(180)

turtle.exitonclick()

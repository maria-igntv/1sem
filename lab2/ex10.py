import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed('fast')

print ('enter numbers of circles')
curcles = int(input())

print('enter radius ')
a = int(input())

def curcle():
    n = 50
    for i in range (n):
        turtle.forward(a*2*(np.pi)/n)
        turtle.left(360/n)

for i in range(curcles):
    curcle()
    turtle.left(360/curcles)

turtle.exitonclick()

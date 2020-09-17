import turtle
import numpy as np


turtle.shape('turtle')

print('enter number of polygons')
n = int(input())
R = 20
for i in range(1, n+1):
    turtle.penup()
    turtle.goto(R*(i), 0)
    turtle.pendown()
    turtle.left(180*(i+4)/(2*(i+2)))
    
    for j in range(i+2):
        turtle.forward(2*R*i*np.sin(np.pi/(i+2)))
        turtle.left(180-180*(i)/(i+2))
    
    
    turtle.right(180-180*(i)/(i+2))
    turtle.right(180*(i)/(2*(i+2)))


turtle.exitonclick()

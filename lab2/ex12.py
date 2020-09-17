import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(0)

print('enter number of iterations')
quant_curcles = int(input())

def half_curcle(a):
    n = 50
    for i in range (n//2):
        turtle.forward(a*2*(np.pi)/n)
        turtle.left(360/n)

turtle.left(90)
for i in range(quant_curcles):
    half_curcle(15)
    half_curcle(40)

turtle.exitonclick()

import turtle
import numpy as np

turtle.shape('turtle')

print('enter number of turns')
turns = int(input())
alpha = 36

for i in range (turns*alpha):
    turtle.forward(i*2* (np.pi) / alpha)
    turtle.left(360/alpha)

turtle.exitonclick()

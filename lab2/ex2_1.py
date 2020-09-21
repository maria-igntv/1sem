import turtle

turtle.shape('turtle')

from random import *

for i in range (1, randint(50, 500)):
    turtle.forward(randint(10,50))
    turtle.left(randint(0,360))

turtle.exitonclick()
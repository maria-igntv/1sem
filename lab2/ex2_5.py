from random import randint, random
import turtle
#turtle.speed('fast')

number_of_turtles = 15
dt = 0.75

pool = [[turtle.Turtle(shape='circle'), randint(-150, 150), randint(-150, 150), 
         randint(-15, 15), randint(-15, 15)]
        
    for i in range(number_of_turtles)]

for unit in pool:
    unit[0].penup()
    unit[0].speed(0)
    unit[0].goto(unit[1], unit[2])
    
while True:
    for unit in pool:
        unit[1] += unit[3]*dt
        unit[2] += unit[4]*dt
        unit[0].goto(unit[1], unit[2])
        
        if abs(unit[2]) >= 150:
            unit[4] *= -1.04
        if abs(unit[1]) >= 150:
            unit[3] *= -1.1
            

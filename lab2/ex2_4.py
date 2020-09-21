import turtle

turtle.shape('circle')

turtle.penup()
turtle.goto(-300,-150)
turtle.pendown()
turtle.forward(800)
turtle.goto(-300,-150)

ay = - 9.8
dt = 0.1

x, y, Vx, Vy = -300, 0, 10, 10

while True:
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2 
    Vy += ay*dt
    turtle.goto(x, y)
    if abs(y) >= 150:
        Vy /= -1.05
    if x >= 1000:
        Vx /= -1

turtle.exitonclick()
    

import turtle

print('enter number')
n = int(input())
turtle.shape('turtle')
turtle.shapesize(2)

for step in range(n):
    turtle.forward(10)
    turtle.left(360 / n)
    
turtle.exitonclick()

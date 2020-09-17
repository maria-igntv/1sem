#вложенные квадраты
import turtle

turtle.shape('turtle')
print ('enter number of squares')
n = int(input())
print ('enter length')
l = int(input())
print ('enter step')
s = int(input())
i = 1


while i <= n :
    
    for step in range(4):
        turtle.forward(l)
        turtle.left(90)
        
    turtle.penup()
    
    turtle.right(90)
    turtle.forward(s/2)
    turtle.right(90)
    turtle.forward(s/2)
    turtle.left(180)
    
    turtle.pendown()
    
    l += s
    i +=1

turtle.exitonclick()

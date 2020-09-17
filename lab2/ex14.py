import turtle

turtle.shape('turtle')

print('enter number 7 or 11')
n = int(input())
print('enter length')
l = int(input())

def draw_star(n, l):
    for i in range(n):
       turtle.forward(l)
       turtle.left(180 - 180/n)

draw_star(n, l)

turtle.exitonclick()

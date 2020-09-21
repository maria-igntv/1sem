import turtle

turtle.shape('arrow')
turtle.speed('fast')

print('enter height of numbers')
a = int(input())
print('enter a zip code (6 digits)')
x = input()

turtle.penup()
turtle.goto(-3*a,a//2)
turtle.pendown()
 
def draw_zero (a : int):
    for i in range (2) :
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(2*a)
        turtle.right(90)
        
    turtle.penup()
    turtle.forward(a)
    turtle.pendown()
    
    turtle.penup()
    turtle.forward(a)
    turtle.pendown()

def draw_one (a : int):
    turtle.penup()
    turtle.right(90)
    turtle.forward(a)
    turtle.left(135)
    
    turtle.pendown()
    turtle.forward(a*(2**0.5))
    turtle.right(135)
    turtle.forward(2*a)
    
    turtle.penup()
    turtle.right(180)
    turtle.forward(2*a)
    
    turtle.right(90)
    turtle.penup()
    turtle.forward(a)
    turtle.pendown()

def draw_two (a :int):
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a*(2**0.5))
    turtle.left(135)
    turtle.forward(a)

    turtle.penup()
    turtle.left(90)
    turtle.forward(2*a)
    turtle.right(90)
    turtle.forward(a)
    turtle.pendown()
    
    
def draw_four (a : int):
    turtle.right(90)
    for i in range (3) :
        turtle.forward(a)
        turtle.left(90)
        
    turtle.left(90)
    turtle.forward(2*a)
    
    turtle.penup()
    turtle.right(180)        
    turtle.forward(2*a)
    
    turtle.right(90)
    turtle.forward(a)
    turtle.pendown()
    
def draw_seven (a : int):
    turtle.pendown()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.left(45)
    turtle.forward(a)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(2*a)
    turtle.right(90)
    
    turtle.penup()
    turtle.forward(a)
    turtle.pendown()

numbers = ['0', '1', '2', '3', '4','5', '6', '7']


for i in range (len(x)):
    digit = int(x[i])
    
    if digit == numbers.index('0'):
        draw_zero(a)
    if digit == numbers.index('1'):
        draw_one(a)
    if digit == numbers.index('2'):
        draw_two(a)
    if digit == numbers.index('4'):
        draw_four(a)
    if digit == numbers.index('7'):
        draw_seven(a)
    
turtle.exitonclick()

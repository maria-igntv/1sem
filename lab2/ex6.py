import turtle

turtle.shape('turtle')
print ('enter number of line segments')
n = int(input())
print ('enter length of line')
s = int(input())
i = 1

turtle.right(360/n)

while i <= n :  
    
    turtle.forward(s)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(s)
    turtle.right(180)
    turtle.right(360/n)
    
    i +=1
input()  

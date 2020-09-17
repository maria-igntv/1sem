#квадратная спираль
import turtle

turtle.shape('turtle')
print('enter number of iterations (>=10)')
n = int(input())
print('enter starting length ')
l = int(input())
print('enter step ')
s = int(input())
i = 1


while i <= n :
    
    for step in range(2):
        turtle.forward(l)
        turtle.left(90)
        
    l += s
    i +=1
input()  

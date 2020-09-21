import turtle
turtle.shape('turtle')
  
def draw_number(n):
    if n == '0':
        for line in zero:
            eval(line.rstrip())            
    if n == '1':
        for line in one:
            eval(line.rstrip())
    if n == '2':
        for line in two:
            eval(line.rstrip())
    if n == '4':
        for line in four:
            eval(line.rstrip())
    if  n == '7':
        for line in seven:
            eval(line.rstrip())

with open('0.txt') as file:
    zero = file.readlines()
with open('1.txt') as file:
    one = file.readlines()
with open('2.txt') as file:
    two = file.readlines() 
with open('4.txt') as file:
    four = file.readlines()
with open('7.txt') as file:
    seven = file.readlines()
    
print('enter index')
x = input()

for i in range(len(x)):
    digit = int(x[i])
    draw_number(digit)

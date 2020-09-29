import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

#(x0, y0) = (0, 0)

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
grey = (128, 128, 128)
green = (0, 255, 0)
skyblue = (135, 206, 250)
olive = (128, 128, 0)
brown = (184, 134, 11)
ckota = (205, 133, 63)
pink = (255, 192, 203)

width = 1

screen.fill(brown)

y_wall = 150

def draw_background(color, y_wall, scr_width, height):
    rect (screen, color,(0, y_wall, scr_width, height-y_wall))
    return    

def draw_window(x0, y_wall, y_window, x_window):
    print('enter number of windows')
    number = int(input())
    print('enter space between windows')
    space = int(input())
    a = (y_wall-y_window)//2
    b =  x_window//3
    for i in range(number):
        rect (screen, white, (x0, a, x_window, y_window))
        rect (screen, skyblue, (x0+b//3, a+b//3 , b, b))
        rect (screen, skyblue, (x0+5*b//3, a+b//3, b, b))
        rect (screen, skyblue, (x0+b//3, a+5*b//3 , b, y_window-2*b))
        rect (screen, skyblue, (x0+5*b//3, a+5*b//3 , b, y_window-2*b))
        x0 += (x_window + space)
    
draw_background(olive, y_wall, 500, 800)
draw_window(10, y_wall, 100, 90)

'''def draw_cat ():
    ellipse (screen, ckota, (340, 330, 120, 80))#hvost
    ellipse (screen, black, (340, 330, 120, 80), width)'''

def draw_cat(screen, color, x_cat, y_cat, x_c, y_c    )
    ellipse(screen, color, (x_c, y_c, x_cat, y_cat))#tulovische
    ellipse(screen, black, (x_c, y_c, x_cat, y_cat), width)
    
    circle(screen, color, (x_c+x_cat*17//19, ), 50)#pravlap
    circle(screen, black, (340, 460), 50, width)

ellipse(screen, color, (360, 480, 30, 80))#pravlap  
ellipse(screen, black, (360, 480, 30, 80), width)

ellipse(screen, color, (110, 445, 100, 60))#levay lapa
ellipse(screen, black, (110, 445, 100, 60), width)

ellipse(screen, color, (60, 400, 30, 80))#lapapodgolovoi
ellipse(screen, black, (60, 400, 30, 80), width)


circle (screen, color, (100, 400), 60)#golova
circle (screen, black, (100, 400), 60, width)

circle (screen, green, (70, 400), 15)#levglaz
circle (screen, black, (70, 400), 15, width)

circle (screen, green, (130, 400), 15)#pravglaz
circle (screen, black, (130, 400), 15, width)

ellipse (screen, black, (72, 388, 8, 20))#levzrach(OK)

ellipse (screen, black, (132, 388, 8, 20))#pravzrach(OK)

polygon (screen, pink, [(100, 418),(94, 410),(106, 410)])#nose
polygon (screen, black, [(100, 418),(94, 410),(106, 410)], width)

polygon (screen, color, [(40, 330), (80, 350), (60,370)])#levyxo
polygon (screen, black, [(40, 330), (80, 350), (60,370)], width)

polygon (screen, color, [(120, 350), (140, 370), (160,330)])#pravyxo
polygon (screen, black, [(120, 350), (140, 370), (160,330)], width)

polygon (screen, pink, [(50, 340), (70, 350), (60,360)])#levyxovnutr
polygon (screen, black, [(50, 340), (70, 350), (60,360)], width)

polygon (screen, pink, [(150, 340), (130, 350), (140,360)])#pravyxovnutr
polygon (screen, black, [(150, 340), (130, 350), (140,360)], width)

line (screen, black, [100, 418], [100, 432])#huinypodnosom

arc (screen, black, (86, 425, 14, 14), 7*(np.pi)/6, 2*np.pi)#levus

arc (screen, black, (100, 425, 14, 14), np.pi, 11*np.pi/6)#prus

circle (screen, grey, (280, 580), 60)



pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
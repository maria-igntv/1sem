import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
scr_width = 600
height = 700
screen = pygame.display.set_mode((scr_width, height))

(x0, y0) = (0, 0)

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

def draw_background(color, y_wall):
    '''
    Function paints background
    color - color of background
    y_wall - height of paonted part of background
    '''
    rect (screen, color,(0, y_wall, scr_width, height-y_wall))
    return    

def draw_window(x0, y_wall, y_window, x_window):
    '''
    Functions draws windows 
    x0 - starting point of drawing
    y_wall - height of printed part of the wall
    y_window - height of the window
    x_window - width of the window
    '''
    number = 4 #number of windows
    space = 45 #space between windows 
    a = (y_wall-y_window)//2
    b =  x_window//3
    for i in range(number):
        rect (screen, white, (x0, a, x_window, y_window))
        rect (screen, skyblue, (x0+b//3, a+b//3 , b, b))
        rect (screen, skyblue, (x0+5*b//3, a+b//3, b, b))
        rect (screen, skyblue, (x0+b//3, a+5*b//3 , b, y_window-2*b))
        rect (screen, skyblue, (x0+5*b//3, a+5*b//3 , b, y_window-2*b))
        x0 += (x_window + space)
    
draw_background(olive, y_wall)
draw_window(10, y_wall, 100, 90)

def draw_tail (color, x_mid, y_mid, x_cat, y_cat):
    '''
    Function draws cat's tail
    color - cat's color
    x_mid - x coordinate of cat's body
    y_mid - y coordinate of cat's body
    x_cat - length of cat
    y_cat - height of cat
    '''
    surf = pygame.Surface((x_cat*4 // 7, y_cat // 2))#hvost
    surf.set_colorkey(black)
    ellipse(surf, color, (0 ,0 , x_cat *4// 7, y_cat // 2))
    oldCenter = (x_mid + x_cat * 4 // 7, y_mid + y_cat //5)
    rotatedSurf = pygame.transform.rotate(surf, 330)
    rotEllipse = rotatedSurf.get_rect()
    rotEllipse.center = oldCenter
    screen.blit(rotatedSurf, rotEllipse)

    surf = pygame.Surface((x_cat*4 // 7, y_cat // 2))#hvost
    surf.set_colorkey(black)
    ellipse(surf, (0, 0, 1), (0 ,0 , x_cat*4 // 7, y_cat // 2), width)
    oldCenter = (x_mid + x_cat * 4 // 7, y_mid + y_cat //5)
    rotatedSurf = pygame.transform.rotate(surf, 330)
    rotEllipse = rotatedSurf.get_rect()
    rotEllipse.center = oldCenter
    screen.blit(rotatedSurf, rotEllipse)

def draw_body (color, x_mid, y_mid, x_cat, y_cat):
    '''
    Function draws cat's body
    color - cat's color
    x_mid - x coordinate of cat's body
    y_mid - y coordinate of cat's body
    x_cat - length of cat
    y_cat - height of cat
    '''
    ellipse (screen, color, (x_mid - x_cat // 2, y_mid - y_cat // 2, x_cat, y_cat)) #body
    ellipse (screen, black, (x_mid - x_cat // 2, y_mid - y_cat // 2, x_cat, y_cat), width)
    
    circle (screen, color, (x_mid + x_cat*5 // 14, y_mid + y_cat *3 // 8), x_cat*5 // 28) #paw
    circle (screen, black, (x_mid + x_cat*5 // 14, y_mid + y_cat *3 // 8), x_cat*5 // 28, width)

    ellipse (screen, color, (x_mid + x_cat * 3 // 7 , y_mid + y_cat // 2, x_cat *3 // 28, y_cat // 2))
    ellipse (screen, black, (x_mid + x_cat * 3 // 7, y_mid + y_cat // 2, x_cat *3 // 28, y_cat // 2), width)

    ellipse (screen, color, (x_mid - x_cat*13 // 28, y_mid + y_cat * 9//32, x_cat * 5// 14, y_cat*3 // 8))
    ellipse (screen, black, (x_mid - x_cat*13 // 28, y_mid + y_cat * 9//32, x_cat * 5// 14, y_cat*3 // 8), width)

    ellipse (screen, color, (x_mid - x_cat * 9 //14, y_mid, x_cat *3 // 28, y_cat // 2)) #paw under the head
    ellipse (screen, black, (x_mid - x_cat * 9 //14, y_mid, x_cat *3 // 28, y_cat // 2), width)    

def draw_head (color, x_mid, y_mid, x_cat, y_cat):
    '''
    Function draws cat's head
    color - cat's color
    x_mid - x coordinate of cat's body
    y_mid - y coordinate of cat's body
    x_cat - length of cat
    y_cat - height of cat
    '''
    circle(screen, color, (x_mid - x_cat // 2, y_mid), x_cat//6)
    circle(screen, black, (x_mid - x_cat // 2, y_mid), x_cat//6, width)
    
def draw_eyes (color, x_mid, y_mid, x_cat, y_cat):
    '''
    Function draws cat's eyes
    color - cat color
    x_mid - x coordinate of cat's body
    y_mid - y coordinate of cat's body
    x_cat - length of cat
    y_cat - height of cat
    '''
    circle (screen, color, (x_mid - x_cat // 2 - x_cat // 12, y_mid), x_cat//24)#levglaz
    circle (screen, black, (x_mid - x_cat // 2 - x_cat // 12, y_mid), x_cat//24, width)

    circle (screen, color, (x_mid - x_cat // 2 + x_cat // 12, y_mid), x_cat//24)#levglaz
    circle (screen, black, (x_mid - x_cat // 2 + x_cat // 12, y_mid), x_cat//24, width)

    ellipse (screen, black, (x_mid - x_cat // 2 - x_cat // 12, y_mid - y_cat // 16, x_cat//35, y_cat//8))
    ellipse (screen, black, (x_mid - x_cat // 2 + x_cat // 12, y_mid - y_cat // 16, x_cat//35, y_cat//8))

    x = (x_mid - x_cat // 2)
    a = x_cat // 40
    b = y_cat // 10
    polygon (screen, pink, [(x, y_mid + b),(x - a, y_mid),(x + a, y_mid)])#nose
    polygon (screen, black, [(x, y_mid + b),(x - a, y_mid),(x + a, y_mid)], width)

    line (screen, black, (x, y_mid + b), (x, y_mid + 2*b))

    arc (screen, black, (x-a, y_mid + 3*b, b, b), 7*(np.pi)/6, 2*np.pi)#levus

    arc (screen, black, (x, y_mid + 3*b, b, b), np.pi, 11*np.pi/6)#prus


def draw_ball(x_mid, y_mid, x_cat, y_cat):
    '''
    Function draws ball
    x_mid - x coordinate of cat's body
    y_mid - y coordinate of cat's body
    x_cat - length of cat
    y_cat - height of cat
    '''
    circle (screen, grey, (x_mid, y_mid + y_cat), x_cat // 7)
    circle (screen, black, (x_mid, y_mid + y_cat), x_cat // 7, width)

def draw_ears(color, x_mid, y_mid, x_cat, y_cat):
    '''
    Function draws cat's ears
    color - cat's color
    x_mid - x coordinate of cat's body
    y_mid - y coordinate of cat's body
    x_cat - length of cat
    y_cat - height of cat
    '''
    a = x_cat // 14 
    b = y_cat // 8 
    x = x_mid - (x_cat // 2)
    y = y_mid - y_cat //3
    
    polygon (screen, color, [(x-3*a, y - b), (x - a, y), (x - 2*a, y + b)])#levyxo
    polygon (screen, black, [(x-3*a, y - b), (x - a, y), (x - 2*a, y + b)], width)

    polygon (screen, color, [(x + a, y), (x + 2*a, y + b), (x + 3*a, y - b)])#pravyxo
    polygon (screen, black, [(x + a, y), (x + 2*a, y + b), (x + 3*a, y - b)], width)


x_mid = [400, 140, 270]
y_mid = [280, 300, 450]
x_cat = [100, 200, 150]
y_cat = [40, 80, 60]
color = [white, ckota, grey]

for i in range(len(x_mid)):
    draw_tail(color[i], x_mid[i], y_mid[i], x_cat[i], y_cat[i])
    draw_body(color[i], x_mid[i], y_mid[i], x_cat[i], y_cat[i])
    draw_head(color[i], x_mid[i], y_mid[i], x_cat[i], y_cat[i])
    draw_eyes(green, x_mid[i], y_mid[i], x_cat[i], y_cat[i])
    draw_ball (x_mid[i], y_mid[i], x_cat[i], y_cat[i])
    draw_ears(color[i], x_mid[i], y_mid[i], x_cat[i], y_cat[i])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

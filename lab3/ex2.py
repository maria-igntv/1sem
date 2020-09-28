import pygame, sys
from pygame.draw import *

pygame.init()

FPS = 30

x_screen = 500
y_screen = 600
screen = pygame.display.set_mode((x_screen, y_screen))

white = (255,255,255)
screen.fill(white)

silver = (192, 192, 192)
gray = (128, 128, 128)
red = (255, 0, 0)
black = (0, 0, 0)
dodger_blue = (30, 144, 255)
gainsboro = (220, 220, 220)
tan = (210, 180, 140)
maroon = (128, 0, 0)
brown = (165, 42, 42)
teal = (0, 128, 128)

rect(screen, silver, (0, 0, x_screen, y_screen/2))

#house
circle(screen, silver, (150, 375), 125)
circle(screen, black, (150, 375), 125, 2)
arc(screen, black, (50, 260, 215, 30), 3.8, 5.6)
arc(screen, black, (25, 295, 263, 40), 3.6, 5.8)
line(screen, black, (25, 373), (275, 373))
arc(screen, black, (150, 250, 50, 50), 5.7, 6.8)
arc(screen, black, (105, 250, 40, 50), 2.5, 3.6)
arc(screen, black, (150, 263, 120, 100), 2.7, 3.5)
arc(screen, black, (70, 260, 120, 100), 2.7, 3.5)
arc(screen, black, (185, 260, 50, 100), 5.9, 6.9)
arc(screen, black, (115, 320, 50, 80), 2.4, 3.7)
arc(screen, black, (45, 315, 50, 80), 2.3, 3.9)
arc(screen, black, (165, 320, 50, 80), 5.6, 7.1)


rect(screen, white, (0, 375, x_screen, y_screen/2))

#cat
#paws
#1
surf = pygame.Surface((70, 15))
surf.set_colorkey(black)
ellipse(surf, silver, (0 ,0 , 70, 15))
oldCenter = (70, 505)
rotatedSurf = pygame.transform.rotate(surf, 190)
rotEllipse = rotatedSurf.get_rect()
rotEllipse.center = oldCenter
screen.blit(rotatedSurf, rotEllipse)
#2
surf = pygame.Surface((70, 15))
surf.set_colorkey(black)
ellipse(surf, silver, (0 ,0 , 70, 15))
oldCenter = (90, 520)
rotatedSurf = pygame.transform.rotate(surf, 200)
rotEllipse = rotatedSurf.get_rect()
rotEllipse.center = oldCenter
screen.blit(rotatedSurf, rotEllipse)
#3
surf = pygame.Surface((70, 15))
surf.set_colorkey(black)
ellipse(surf, silver, (0 ,0 , 70, 15))
oldCenter = (170, 520)
rotatedSurf = pygame.transform.rotate(surf, 330)
rotEllipse = rotatedSurf.get_rect()
rotEllipse.center = oldCenter
screen.blit(rotatedSurf, rotEllipse)
#4
surf = pygame.Surface((70, 15))
surf.set_colorkey(black)
ellipse(surf, silver, (0 ,0 , 70, 15))
oldCenter = (200, 515)
rotatedSurf = pygame.transform.rotate(surf, 340)
rotEllipse = rotatedSurf.get_rect()
rotEllipse.center = oldCenter
screen.blit(rotatedSurf, rotEllipse)

#tail
surf = pygame.Surface((80, 20))
surf.set_colorkey(black)
ellipse(surf, silver, (0 ,0 , 80, 20))
oldCenter = (220, 470)
rotatedSurf = pygame.transform.rotate(surf, 30)
rotEllipse = rotatedSurf.get_rect()
rotEllipse.center = oldCenter
screen.blit(rotatedSurf, rotEllipse)

#ears
polygon(screen, silver, ((60, 465), (65, 450), (70, 465), (60, 465)))
polygon(screen, silver, ((85, 465), (95, 450), (100, 465), (85, 465)))
#body
ellipse(screen, silver, (75, 475, 125, 40))
ellipse(screen, silver, (50, 460, 55, 30))
circle(screen, white, (63, 470), 7)
circle(screen, white, (85, 475), 7)
circle(screen, black, (68, 470), 4)
circle(screen, black, (90, 475), 4)

#human
#right arm
surf = pygame.Surface((80, 25))
surf.fill(white)
ellipse(surf, tan, (0 ,0 , 80, 25))
oldCenter = (420, 405)
rotatedSurf = pygame.transform.rotate(surf, 325)
rotEllipse = rotatedSurf.get_rect()
rotEllipse.center = oldCenter
screen.blit(rotatedSurf, rotEllipse)

#body
ellipse(screen, silver, (315, 315, 125, 65))
ellipse(screen, tan, (325, 350, 100, 200))
ellipse(screen, brown, (325, 325, 105, 50))
ellipse(screen, gainsboro, (340, 335, 75, 35))
line(screen, black, (365, 350), (350, 343), 2)
line(screen, black, (385, 350), (400, 347), 2)
arc(screen, black, (355, 358, 40, 10), 0.3, 2.6)
rect(screen, white, (325, 450, x_screen // 2, y_screen // 2))

#legs
ellipse(screen, tan, (340, 425, 30, 75))
ellipse(screen, tan, (380, 425, 30, 75))

#left arm
ellipse(screen, tan, (295, 385, 80, 25))
line(screen, black, (305, 310), (305,485))
line(screen, maroon, (375, 370), (375,440), 25)
rect(screen, maroon, (325, 445, 100, 20))

#feet
ellipse(screen, tan, (330, 485, 40, 15))
ellipse(screen, tan, (380, 485, 40, 15))

#fish
polygon(screen, red, ((50, 485), (55, 490), (55, 495), (60, 490)))
polygon(screen, red, ((50, 480), (45, 470), (55, 475), (60, 480)))

surf = pygame.Surface((45, 10))
surf.set_colorkey(black)
ellipse(surf, teal, (0 ,0 , 45, 10))
oldCenter = (60, 485)
rotatedSurf = pygame.transform.rotate(surf, 340)
rotEllipse = rotatedSurf.get_rect()
rotEllipse.center = oldCenter
screen.blit(rotatedSurf, rotEllipse)
polygon(screen, teal, ((80, 492), (100, 492), (90, 502), (80, 492)))
circle(screen, black, (46, 480), 3)

line(screen, white, (65, 480), (70, 490), 2)
line(screen, white, (70, 480), (75, 490), 2)
ellipse(screen, silver, (58, 478, 30, 10))
circle(screen, black, (70, 480), 2)
#ellipse(screen, black, (58, 480, 30, 10),1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

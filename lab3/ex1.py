import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

background_colour = (255,255,255)
screen.fill(background_colour)

yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

circle(screen, yellow, (250, 250), 150)
circle(screen, black, (250, 250), 150, 2)

circle(screen, red, (325,225), 30)
circle(screen, red, (175,225), 30)
circle(screen, black, (325, 225), 30, 2)
circle(screen, black, (175, 225), 30, 2)

circle(screen, black, (175, 225), 15)
circle(screen, black, (325, 225), 15)

rect(screen, black, (175, 310, 150, 20))

line(screen, black, (275, 215), (410, 160), 15)
line(screen, black, (225, 215), (75, 125), 15)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

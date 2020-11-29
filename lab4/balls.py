import pygame
from pygame.draw import *
from random import randint
from math import *


name = input('Enter your name: ')

pygame.init()

# let's define colors of our balls
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)
colors = [red, blue, yellow, green, magenta, cyan]


offences_bank = []
offencive_file = open('players.txt', 'r+')
for line in offencive_file:
    offences_bank.append(line)



num = 3
radius_min = 20
radius_max = 100
width = 1200
height = 600
FPS = 100
screen = pygame.display.set_mode((width, height))
#pygame.time.delay(2000)
screen.fill(black)
pygame.display.update()

my_font = pygame.font.SysFont('Times New Roman', 50)


def new_balls(num): # this function draws num balls
    global x, y, r, vx, vy, color, count 
    count = 0
    x = []
    y = []
    r = []
    vx = []
    vy = []
    color = []
    for i in range(num):
        x.append(randint(radius_max, width - radius_max))
        y.append(randint(radius_max, height - radius_max))
        r.append(randint(radius_min, radius_max))
        vx.append(randint(500,1000))
        vy.append(randint(500,1000))
        color.append(colors[randint(0, 5)])


def respawn():  # this function creates a new ball if player clicked successfully
    x.append(randint(radius_max, width - radius_max))
    y.append(randint(radius_max, height - radius_max))
    r.append(randint(radius_min, radius_max))
    vx.append(randint(500,1000))
    vy.append(randint(500,1000))
    color.append(colors[randint(0, 5)])
    circle(screen, color[len(color) - 1], (x[len(x) - 1], y[len(y) - 1]), r[len(r) - 1])


def move_balls(num):  # this function moves our balls
    for i in range(num):
        x[i] += vx[i] // FPS
        y[i] += vy[i] // FPS


def draw_balls(num):
    for i in range(num):
        circle(screen, color[i], (x[i], y[i]), r[i])


def hit_check(num):  # this function checks if the ball hit the wall and turns it back
    for i in range(num):
        if x[i] + r[i] > width or x[i] - r[i] < 0:
            vx[i] = -vx[i]
            x[i] += vx[i] // FPS
            print(x[i], r[i], vx[i])
        if y[i] + r[i] > height or y[i] - r[i] < 0 :
            vy[i] = - vy[i]
            y[i] += vy[i] // FPS


def check_click(event, num):  # this function checks if the player clicked successfully
    global count, x, y, r, v, color
    coord = event.pos
    for i in range(num):
        if (x[i] - coord[0]) ** 2 + (y[i] - coord[1]) ** 2 <= r[i] ** 2:
            count += 1
            x.remove(x[i])
            y.remove(y[i])
            r.remove(r[i])
            vx.remove(vx[i])
            vy.remove(vy[i])
            color.remove(color[i])
            return True
    return False
    

#def create_running_string:
    


pygame.display.update()
clock = pygame.time.Clock()

new_balls(4)
finished = False

while not finished:
    screen.fill(black)
    clock.tick(FPS)
    move_balls(len(x))
    hit_check(len(x))
    draw_balls(len(x))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(event, len(x)):
                respawn()

    string = "Удачных попаданий: " + str(count)
    text_color = yellow
    text = my_font.render(string, 1, text_color)
    screen.blit(text, (3, 3))
    pygame.display.update()

pygame.quit()

n_player = [name, count]
players = []

with open('players.txt', 'r+') as file:
    for s in file:
        players.append(s.split())
    players.append(n_player)
    for player in players:
        player[1] = int(player[1])
    players = sorted(players, key = lambda player: player[1], reverse = True)
    file.seek(0)
    file.truncate()
    for player in players:
        player = str(player[0]) + ' ' + str(player[1]) + '\n'
        file.write(player)




    



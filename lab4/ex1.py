import pygame
from pygame.draw import *
from random import randint

gamer_name = input('Enter yor name: ')

pygame.init()

FPS = 60
screen = pygame.display.set_mode((800, 500))

def new_ball(screen_ball: pygame.Surface, x_ball: int, y_ball: int, r_ball: int, color_ball: tuple):
    '''
    Function draws a ball.
    screen_ball - pygame.Surface of the game display
    x_ball -  x-coordinate of the ball's center
    y_ball -  y-coordinate of the ball's center
    r_bal -  radius of the ball
    color_ball - color of the ball
    '''
    circle(screen_ball, color_ball, (x_ball, y_ball), r_ball)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
k = 0  # score counter
balls = []  # list of coordinates and other characteristics of usual balls
timer = 0  # 'time' of the game

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.draw.rect(screen,(60,25,60), [370, 240, 170, 60])
            f = pygame.font.Font(None, 50)
            text = f.render('Score: ' + str(k), 1, (255,255,255))
            screen.blit(text, (380, 250))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x_mouse, y_mouse) = event.pos  # coordinates of the mouse
            # condition for hitting the ball
            for ball in balls:
                if (ball[0] - x_mouse) ** 2 + (ball[1] - y_mouse) ** 2 <= ball[2] ** 2:
                    k += 1  # counting of score
                    balls.remove(ball)  # disappearance of the shot ball

    # movement of balls
    for ball in balls:
        ball[0] += ball[4]
        ball[1] += ball[5]
        # conditions of reflection from the walls
        if (ball[0] + ball[2] > 800) or (ball[0] - ball[2] < 0):
            ball[4] *= -1
        if (ball[1] + ball[2] > 500) or (ball[1] - ball[2] < 0):
            ball[5] *= -1
        # condition for disappearing if the ball is old
        if ball[6] < 150 and not ball[7]:
            new_ball(screen, ball[0], ball[1], ball[2], ball[3])
            ball[6] += 1
        else:
            del ball

    
    # appearance of a new ball
    if timer % 20 == 0:
        x = randint(100, 600)
        y = randint(100, 350)
        r = randint(10, 75)
        dx = randint(-5, 5)
        dy = randint(-5, 5)
        lifetime = 0
        click = False
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        balls.append([x, y, r, color, dx, dy, lifetime, click])
        new_ball(screen, x, y, r, color)

    timer += 1  # counting time of the game
    pygame.display.update()
    clock.tick(FPS)
    screen.fill((0, 0, 0))  # updating the display

pygame.quit()

new_gamer = [gamer_name, k]
gamers = []  # list of gamers and their scores

# building of the list of gamers
with open('gamers.txt', 'r+') as file:
    for s in file:  # reading from the file
        gamers.append(s.split())
    gamers.append(new_gamer)
    for gamer in gamers:
        gamer[1] = int(gamer[1])
    gamers = sorted(gamers, key=lambda gamer: gamer[1], reverse=True)  # sorting of records
    file.seek(0)  # clearing of the file
    file.truncate()
    for gamer in gamers:
        gamer = str(gamer[0]) + ' ' + str(gamer[1]) + '\n'
        file.write(gamer)

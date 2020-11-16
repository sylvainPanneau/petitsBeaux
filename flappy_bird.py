import pygame
from random import *
import time

class bird:
    def __init__(self, y):
        self.y = y

    def trajectory(self, time):
        if time < time_increment*2000: # faut revoir l'équation et mettre un clock au lieu de time_increment comme ça
            self.y = -0.5*9.81*time*time
        elif time < time_increment*4000:
            self.y = 0.5*9.81*time*time
        else:
            return 0
        return self.y
class pipe:
    def __init__(self, x, y):
        self.y = y
        self.x = x

pipe = pipe(400, 350)
bird = bird(230)
time = 0
time_increment = 0.00001

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((800, 600))
pygame.display.update()
black = (0,0,0)
red = (255,0,0)
green = (0,200,100)
white = (200, 200, 200)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    print(event)
    pipe.x+=-0.09
    time += time_increment
    dis.fill(white)
    bird.y += bird.trajectory(time)
    pygame.draw.rect(dis, green, [pipe.x, 350 , 60, 250])
    pygame.draw.rect(dis, red, [80, bird.y, 22, 22])
    pygame.display.update()

pygame.quit()
quit()
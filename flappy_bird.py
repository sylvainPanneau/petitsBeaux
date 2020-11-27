import pygame
from random import *
import time

class bird:
    def __init__(self, y):
        self.y = y
    
    def trajectory(self, time):
        self.y = (-0.5*time*time)+200
        return self.y

class pipe:
    def __init__(self, x, y):
        self.y = y
        self.x = x

pipe = pipe(400, 350)
bird = bird(230)
time = 0

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
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
                


    print(event)
    pipe.x+=-0.09
    dis.fill(white)
    time+=0.1
    bird.y = bird.trajectory(time)
    pygame.draw.rect(dis, green, [pipe.x, 350 , 60, 250])
    pygame.draw.rect(dis, red, [80, abs(bird.y), 22, 22])
    pygame.display.update()

pygame.quit()
quit()
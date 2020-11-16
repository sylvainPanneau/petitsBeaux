import pygame
import time
from random import *

pygame.init()
dis = pygame.display.set_mode((800, 600))
dis_width = 800
dis_height = 600
pygame.display.update()

game_over = False

x = 0
y = 0

x1_change = 0
y1_change = 0

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

applex = randint(0, dis_width//10)*10
appley = randint(0, dis_height//10)*10


def message(msg, color):
    message = font_style.render(msg, True, color)
    dis.blit(message, [dis_width/4, dis_height/2])


blue = (0, 180, 255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()

snake_list = []
length_snake = 1


def long_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], 10, 10])


def score(length_snake):
    msg = "Score : " + str(length_snake)
    score_string = score_font.render(msg, True, black)
    dis.blit(score_string, [dis_width/30, dis_height/30])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
    if x > dis_width or x < 0 or y > dis_height or y < 0:
        game_over = True
    if x == applex and y == appley:
        applex = randint(0, dis_width//10)*10
        appley = randint(0, dis_height//10)*10
        length_snake += 1

    x += x1_change
    y += y1_change
    dis.fill(blue)
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)
    pygame.draw.rect(dis, red, [applex, appley, 10, 10])

    if length_snake < len(snake_list):
        del snake_list[0]

    for slt in snake_list[:-1]:
        if slt == snake_head:
            game_over = True

    long_snake(snake_list)
    score(length_snake)
    pygame.display.update()

    clock.tick(30)

message("you lost son of a mom", black)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
import pygame as pg
import pygame.time
from pygame import *
import sys

SIZE_CELL = 16
HEIGHT_CELL = 60
WIDTH_CELL = 45
HEIGHT = SIZE_CELL * HEIGHT_CELL
WIDTH = SIZE_CELL * WIDTH_CELL
SNAKE_COLOR_HEAD = (0, 255, 0)
SNAKE_COLOR = (0, 0, 255)


clock = pygame.time.Clock()
sc = pg.display.set_mode((HEIGHT,WIDTH))

snake = [[HEIGHT_CELL // 2, WIDTH_CELL // 2],
         [HEIGHT_CELL // 2, WIDTH_CELL // 2 + 1],
         [HEIGHT_CELL // 2, WIDTH_CELL // 2 + 2]]

def draw_snake(snake):
    color = SNAKE_COLOR_HEAD
    for cell in snake:
        pygame.draw.rect(sc, color,
                         (cell[0] * SIZE_CELL,
                         cell[1] * SIZE_CELL,
                         SIZE_CELL, SIZE_CELL))
        color = SNAKE_COLOR

def change_direction(event, direction):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            return [-1,0]
        elif event.key == pygame.K_RIGHT:
            return [1,0]
        elif event.key == pygame.K_UP:
            return [0,-1]
        elif event.key == pygame.K_DOWN:
            return [0,1]
    return direction

def change_pos(direction):
        if (direction != [0,0]):
            snake.insert(0, [snake[0][0] + direction[0],
                             snake[0][1] + direction[1]])
            snake.pop(-1)

direction = [0,0]

while 1:
    for i in pg.event.get():
        if i.type == QUIT:
            sys.exit()
        direction = change_direction(i, direction)

    change_pos(direction)

    sc.fill((0,0,0))
    draw_snake(snake)
    pygame.display.update()
    clock.tick(15)
import pygame
import time
import Small_projects.Langtons_Ant_code
import numpy as np

from Small_projects import Langtons_Ant_code

pygame.init()
clock = pygame.time.Clock()  # FPS stuff
# table = pygame.image.load(r'C:\Users\antho\Desktop\grid.png')
GD = pygame.display.set_mode((200 * 5, 200 * 5))
crashed = False
grid = Langtons_Ant_code.grid


def draw_grid():
    y_ = 0
    for i in range(100):
        x_ = 0
        for i in range(100):
            draw_none_squares(x_, y_)
            x_ += 1
        y_ += 1

    """
    x,y = 0,0
    for i in range(5):
        for i in range(5):
            GD.blit(table, (x, y))
            x+=200
        x=0
        y+=200
    """


def draw_none_squares(x, y):
    x = x * 10 + 1
    y = y * 10 + 1
    pygame.draw.rect(GD, (200, 200, 200), (x, y, 9, 9))


def draw_red_squares(x, y):
    x = x * 10 + 1
    y = y * 10 + 1
    pygame.draw.rect(GD, (255, 0, 0), (x, y, 9, 9))


def draw_white_squares(x, y):
    x = x * 10 + 1
    y = y * 10 + 1
    pygame.draw.rect(GD, (255, 255, 255), (x, y, 9, 9))


def update_grid():
    for i2 in range(len(grid)):
        for i in range(len(grid[i2])):
            if grid[i2][i] == 1:
                draw_red_squares(i, i2)
            elif grid[i2][i] == 2:
                draw_white_squares(i, i2)


def text(text):
    font = pygame.font.SysFont(None, 50)
    img = font.render("step" + str(text), True, (0, 0, 0))
    GD.blit(img, (20, 20))


step = 0

while not crashed:  # makes window not buggy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    # GD.blit(table, (0, 0))
    draw_grid()
    """
    y_=0
    for i in range(37):
        x_ = 0
        for i in range(37):
            draw_red_squares(x_, y_)
            x_+=1
        y_+=1
    pygame.draw.rect(GD, (255, 255, 255), (500, 500, 12, 12))
    """
    step += 1
    text(step)
    update_grid()

    Langtons_Ant_code.ant()
    # time.sleep(0.1)



    pygame.display.update()
    # time.sleep(0.1)
    clock.tick(60)

pygame.quit()

import pygame
import time
import sys
import random

sys.path.append('C:/Users/antho/AppData/Local/Programs/Python/Python38-32/Small_projects/Snake_code')

import Snake_code

pygame.init()
clock = pygame.time.Clock()  # FPS stuff

noneSprite = pygame.image.load(r'C:\Users\antho\Desktop\pyImages\grid.png')
headSprite = pygame.image.load(r'C:\Users\antho\Desktop\pyImages\head.png')
bodySprite = pygame.image.load(r'C:\Users\antho\Desktop\pyImages\body.png')
bendSprite = pygame.image.load(r'C:\Users\antho\Desktop\pyImages\bend.png')
crashed = False

textSpace = 50
size = Snake_code.size
GD = pygame.display.set_mode((size * 2 * 5, size * 2 * 5 + textSpace))
grid = Snake_code.grid
direction = Snake_code.direction
score = Snake_code.score
moved = True
death = False
head_x, head_y = 0, 0
body_x, body_y = [int(size / 2), int(size / 2)], [int(size / 2 - 1), int(size / 2 - 2)]
extreem_mode = False
"""
problems:
when eating the head must like stay in place so like u can eat coners and not die

do the determen body shape code
"""


def main():
    draw_grid()
    update_grid()
    text(score)


def draw_grid():
    GD.blit(noneSprite, (0, 0))


def draw_white_squares(x, y):
    x = x * 10 + 1
    y = y * 10 + 1
    pygame.draw.rect(GD, (255, 255, 255), (x, y, 9, 9))


def drawHead(x, y, angle):
    x = x * 10 + 1
    y = y * 10 + 1
    img = pygame.transform.rotate(headSprite.copy(), angle)
    GD.blit(img, (x, y))


def drawBody(x, y):
    x = x * 10 + 1
    y = y * 10 + 1
    GD.blit(bodySprite, (x, y))


def drawBend(x, y, angle):
    x = x * 10 + 1
    y = y * 10 + 1
    img = pygame.transform.rotate(bendSprite.copy(), angle)
    GD.blit(img, (x, y))


def update_grid():
    d = dict((j, (x, y)) for x, i in enumerate(grid) for y, j in enumerate(i))
    try:
        for i in range(score):
            y, x = d[i + 1]
            draw_white_squares(x, y)
    except:
        print("death")


def text(text):
    font = pygame.font.SysFont(None, 50)
    img = font.render("score: " + str(text), True, (255, 255, 255))
    pygame.draw.rect(GD, (100, 100, 100), (0, size * 2 * 5, size * 2 * 5, textSpace))
    GD.blit(img, (20, size * 2 * 5))


def Gameover():
    font = pygame.font.SysFont(None, 50)
    img = font.render("Game Over ", True, (255, 255, 255))
    GD.blit(img, (size * 5 - 80, size * 5 - 20))


rand_x, rand_y = random.choice([i for i in range(0, size) if i not in body_x + [head_x]]), random.choice(
    [i for i in range(0, size) if i not in body_y + [head_y]])  # write code to not have block spawn on snake
pause, step = True, False
while not crashed:  # makes window not buggy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if moved:
                if event.key == pygame.K_UP and direction != "S":
                    direction = "N"
                    moved = False
                if event.key == pygame.K_DOWN and direction != "N":
                    direction = "S"
                    moved = False
                if event.key == pygame.K_RIGHT and direction != "W":
                    direction = "E"
                    moved = False
                if event.key == pygame.K_LEFT and direction != "E":
                    direction = "W"
                    moved = False
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_x:
                step = not step
    # --------------------------------------------------------------------------------------------------------------------------

    if death == False:
        main()

    if grid[rand_y][rand_x] == score:  # check if head is on eat
        score += 1

        if direction == "N":  # check if point next to wall determens death *fix
            if rand_y == 0:
                death = True
            else:
                grid[rand_y - 1][rand_x] = score

        elif direction == "S":
            if rand_y == size - 1:
                death = True

            else:
                grid[rand_y + 1][rand_x] = score

        elif direction == "E":
            if rand_x == size - 1:
                death = True

            else:
                grid[rand_y][rand_x + 1] = score

        else:
            if rand_x == 0:
                death = True

            else:
                grid[rand_y][rand_x - 1] = score
        if death == False:
            rand_x, rand_y = random.randrange(0, size), random.randrange(0,
                                                                         size)  # write code to not have block spawn on snake

    if death:
        Gameover()

    if pause == False or step == True:
        if death == False:
            test = Snake_code.snake(direction, score, grid)
            death = test.head()
            death = test.body()
            step = False
            moved = True
            head_x, head_y = test.head_x, test.head_y
            body_x, body_y = test.body_x, test.body_y

    draw_white_squares(rand_x, rand_y)
    # --------------------------------------------------------------------------------------------------------------------------

    pygame.display.update()
    if not extreem_mode: time.sleep(0.05)
    clock.tick(60)

pygame.quit()

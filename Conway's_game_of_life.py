import pygame
import time
import Conwys_game_of_life_code

pygame.init()
clock = pygame.time.Clock()  # FPS stuff
GD = pygame.display.set_mode((200 * 5, 200 * 5))
crashed = False
grid = Conwys_game_of_life_code.grid


def draw_grid():
    y_ = 0
    for i in range(100):
        x_ = 0
        for i in range(100):
            draw_none_squares(x_, y_)
            x_ += 1
        y_ += 1


def draw_none_squares(x, y):
    x = x * 10 + 1
    y = y * 10 + 1
    pygame.draw.rect(GD, (50, 50, 50), (x, y, 9, 9))


def draw_white_squares(x, y):
    x = x * 10 + 1
    y = y * 10 + 1
    pygame.draw.rect(GD, (250, 250, 250), (x, y, 9, 9))


def update_grid():
    for i2 in range(len(grid)):
        for i in range(len(grid[i2])):
            if grid[i2][i] == 1:
                draw_white_squares(i, i2)


def text():
    font = pygame.font.SysFont(None, 60)
    img = font.render("ll", True, (255, 255, 255))
    GD.blit(img, (20, 20))


step = 0
start, pause, reset = False, False, False
print("Press R to clear the board, Space to start, and X to go step by step")
while not crashed:  # makes window not buggy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = not start
            if event.key == pygame.K_x:
                pause = not pause
            if event.key == pygame.K_r:
                reset = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = int(x / 10)
            y = int(y / 10)
            if grid[y][x] == 1:
                grid[y][x] = 0
            else:
                grid[y][x] = 1
    GD.fill((110, 110, 110))
    draw_grid()

    x, y = pygame.mouse.get_pos()
    draw_white_squares(int(x / 10), int(y / 10))

    if not start:
        text()
        if reset:
            for i2 in range(len(grid)):
                for i in range(len(grid[i2])):
                    grid[i2][i] = 0
            reset = False
    # --------------------------------------------------------------------------------------------------------------------
    if start == True or pause == True:
        Conwys_game_of_life_code.step()
        pause = False
        reset = False
        # if start:
        # time.sleep(0.5)

    update_grid()

    # --------------------------------------------------------------------------------------------------------------------
    pygame.display.update()
    clock.tick(60)

pygame.quit()

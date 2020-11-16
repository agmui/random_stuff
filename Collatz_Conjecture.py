import pygame
import time
import math
import Collatz_Conjecture_code

pygame.init()
clock = pygame.time.Clock()  # FPS stuff
GD = pygame.display.set_mode((200 * 5, 200 * 5))
crashed = False
tree = Collatz_Conjecture_code.l
_ = -1

def text(text, x, y):
    font = pygame.font.SysFont(None, 20)
    img = font.render(str(text), False, (0, 0, 0))
    GD.blit(img, (x - 3, y - 6))


def draw_circle(old_x, a, num):
    # x should be relative pos of root/ last node
    # a should be relative pos of roo/ last node to find angle

    # needs to calc where new pos and angle based on root/ last node
    # y = a  # ts
    x, y = old_x*math.sin(a), old_x*math.cos(a) # PLLLZZZZ CHECK IF IN RADS OR DEG !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    pygame.draw.circle(GD, (250, 250, 250), (x, y), 5)
    text(num, x, y)
    if num/2 == int(num/2):
        th = a+5
    else:
        th = a-5
    return (x, y), (th,_)


def some_pos_function(x):
    for i in range(len(tree)):
        if tree[i][1] == x or tree[i][2] == x:
            return tree[i][4]


def some_angle_function(x):
    for i in range(len(tree)):
        if tree[i][1] == x or tree[i][2] == x:
            return tree[i][5]


GD.fill((110, 110, 110))  # draw background

i = 0
tree[0][4], tree[0][5] = (50, 50), (270, _)
while not crashed:  # makes window not buggy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    x, a = some_pos_function(tree[i][0]), some_angle_function(tree[i][0])
    new_x, new_a = draw_circle(x, a, tree[i][0])
    tree[i][4], tree[i][5] = new_x, new_a

    i += 1
    time.sleep(1)
    pygame.display.update()
    clock.tick(60)

pygame.quit()

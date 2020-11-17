import pygame
import time
import math
import Collatz_Conjecture_code

pygame.init()
clock = pygame.time.Clock()  # FPS stuff
GD = pygame.display.set_mode((200 * 5, 200 * 5))
crashed = False
tree = Collatz_Conjecture_code.l
_ = -1  # dont use
line_length = 30
angle = 10


def text(text, x, y):
    font = pygame.font.SysFont(None, 20)
    img = font.render(str(text), False, (0, 0, 0))
    GD.blit(img, (x - 3, y - 6))


def draw_better_line(GD, pos1, pos2, thicccness):
    pygame.draw.line(GD, (0, 0, 0), pos1, pos2, thicccness)
    pygame.draw.line(GD, (250, 250, 250), pos1, pos2, thicccness - 2)

def influwence(x,y):
    return 1+abs(x-y)/50000

def draw_circle(old_cords, a, num, help_):
    # x should be relative pos of root/ last node
    # a should be relative pos of roo/ last node to find angle

    # needs to calc where new pos and angle based on root/ last node
    a, _ = a
    old_x, old_y = old_cords
    if num / 2 == int(num / 2):
        a = (angle + a)*influwence(num, tree[help_][0])
    else:
        a = -1 * angle + a
    x, y = -line_length * math.sin(a * math.pi / 180) + old_x, line_length * math.cos(a * math.pi / 180) + old_y
    # pygame.draw.circle(GD, (250, 250, 250), (x, y), 5)
    # text(num, x, y)
    draw_better_line(GD, (old_x, old_y), (x, y), 10)
    return (x, y), (a, _)  # probs needs help


def some_pos_function(x):
    for i in range(len(tree)):
        if tree[i][1] == x or tree[i][2] == x:
            return tree[i][4], i


def some_angle_function(x):
    for i in range(len(tree)):
        if tree[i][1] == x or tree[i][2] == x:
            return tree[i][5]


GD.fill((110, 110, 110))  # draw background

i = 1
tree[0][4], tree[0][5] = (400, 400), (270, _)
draw_circle((450, 401), (270, _), tree[0][0], 0)
while not crashed:  # makes window not buggy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    x, help_ = some_pos_function(tree[i][0])
    a=some_angle_function(tree[i][0])
    new_x, new_a = draw_circle(x, a, tree[i][0], help_)
    tree[i][4], tree[i][5] = new_x, new_a

    i += 1
    # time.sleep(0.01)
    pygame.display.update()
    clock.tick(60)

pygame.quit()

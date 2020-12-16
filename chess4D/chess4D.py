import pygame as py
import sys
import time
from pygame.locals import *

sys.path.insert(1, r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D')
import chess4d_code

py.init()
clock = py.time.Clock()  # FPS stuff
size = 50
GD = py.display.set_mode((size * 8, size * 8))
crashed = False

Bking_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\King.png')
Bqueen_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Queen.png')


def init_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                c = (201, 123, 58)
            else:
                c = (227, 187, 154)
            py.draw.rect(GD, c, (j * size, i * size, size, size))
    # set up chess pieces
    Bking = chess4d_code.piece((size * 4, size * 4), 'King', Bking_pic)  # fine tune
    Bqueen = chess4d_code.piece((size * 4, size * 4), 'King', Bqueen_pic)
    return Bking, Bqueen


while not crashed:  # makes window not buggy
    for event in py.event.get():
        if event.type == py.QUIT:
            crashed = True
        elif event.type == MOUSEBUTTONDOWN:
            mx, my = py.mouse.get_pos()
            px, py = Bking.get_pos()
            if mx >= px and my >= px and mx <= px+50 and my <= px+50:
                print('on')
            else:
                print('off')

    Bking, Bqueen = init_board()

    Bking.move("U")
    Bking.draw1()

    Bqueen.draw1()

    py.display.update()
    clock.tick(60)
py.quit()

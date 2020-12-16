import pygame as py
import time
from pygame.locals import *

py.init()
clock = py.time.Clock()  # FPS stuff
size = 50
GD = py.display.set_mode((size * 8, size * 8))
crashed = False

Bking_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\King.png')
Bqueen_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Queen.png')


class piece:
    def __init__(self, pos, type, img):
        self.pos = pos
        self.type = type
        self.img = img
        self.size = self.img.get_size()

    def draw1(self):
        if self.type == 'p':
            pass
        elif self.type == 'k':
            pass
        elif self.type == 'b':
            pass
        elif self.type == 'r':
            pass
        elif self.type == 'q':
            pass
        elif self.type == 'King':
            king_pic = py.transform.scale(self.img, (50, 50))
            GD.blit(king_pic, self.pos)

    def move(self, dir, amount=1):
        if self.type == 'Wp':
            pass
        if self.type == 'Bp':
            pass
        elif self.type == 'k':
            pass
        elif self.type == 'b':
            pass
        elif self.type == 'r':
            pass
        elif self.type == 'q':
            if dir == 'U':
                self.pos = (self.pos[0], self.pos[1] - 50)
        elif self.type == 'King':
            if dir == 'U':
                self.pos = (self.pos[0], self.pos[1] - 50)

    def get_pos(self):
        return self.pos

def init_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                c = (201, 123, 58)
            else:
                c = (227, 187, 154)
            py.draw.rect(GD, c, (j * size, i * size, size, size))
    # set up chess pieces
    Bking = piece((size * 4, size * 4), 'King', Bking_pic)  # fine tune
    Bqueen = piece((size * 4, size * 4), 'King', Bqueen_pic)
    return Bking, Bqueen

def main():
    global py, crashed, size
    while not crashed:  # makes window not buggy
        for event in py.event.get():
            if event.type == py.QUIT:
                crashed = True
            """elif event.type == MOUSEBUTTONDOWN:
                mx, my = py.mouse.get_pos()
                px, py = Bking.get_pos()
                if mx >= px and my >= px and mx <= px + 50 and my <= px + 50:
                    print('on')
                else:
                    print('off')"""

        Bking, Bqueen = init_board()

        Bking.move("U")
        Bking.draw1()

        Bqueen.draw1()

        py.display.update()
        clock.tick(60)
    py.quit()

main()
import pygame as py
import time

# from pygame.locals import *

py.init()
clock = py.time.Clock()  # FPS stuff
size = 50
GD = py.display.set_mode((size * 8, size * 8))
crashed = False
select = 0

# Bking_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\King.png')
# Bqueen_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Queen.png')

Bking_pic = py.image.load('/Users/Anthony/PycharmProjects/random_stuff/chess4D/assets/King.png')  # .convert_alpha()
Bqueen_pic = py.image.load('/Users/Anthony/PycharmProjects/random_stuff/chess4D/assets/Queen.png')  # .convert_alpha()


class piece:
    def __init__(self, pos, type, img):
        self.pos = pos
        self.type = type
        self.img = img
        self.size = self.img.get_size()

    def draw(self):
        if self.type == 'p':
            pass
        elif self.type == 'k':
            pass
        elif self.type == 'b':
            pass
        elif self.type == 'r':
            pass
        elif self.type == 'q':
            queen_pic = py.transform.scale(self.img, (50, 50))
            GD.blit(queen_pic, self.pos)
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

    def move_check(self):
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
            pass
        elif self.type == 'King':
            return 1, 1


def init_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                c = (201, 123, 58)
            else:
                c = (227, 187, 154)
            py.draw.rect(GD, c, (j * size, i * size, size, size))


# set up chess pieces
Bking = piece((size * 4, size), 'King', Bking_pic)  # fine tune
Bqueen = piece((size * 4, size * 4), 'q', Bqueen_pic)

# list of all pieces
p = [Bking, Bqueen]


def main():
    global py, crashed, size, select
    while not crashed:  # makes window not buggy
        for event in py.event.get():
            if event.type == py.QUIT:
                crashed = True
            elif event.type == py.MOUSEBUTTONDOWN:
                mx, my = py.mouse.get_pos()
                for piece_ in p:
                    x, y = piece_.pos
                    if mx >= x and my >= y and mx <= x + 50 and my <= y + 50:
                        print('on', piece_.type)
                        select = piece_
                    else:
                        print('off', piece_.type)
                        if select != 0 and (dir, amount := select.move_check()) :  # check if possible pos
                            print(dir, amount)
                        else:
                            select = 0
                        """check which is faster
                    if py.Rect(piece_.pos, (piece_.img.get_width(), piece_.img.get_height())).collidepoint(py.mouse.get_pos()):
                        print('on', piece_.type)
                    else:
                        print('off', piece_.type)"""
        init_board()

        # Bking.move("U")
        Bking.draw()

        Bqueen.draw()

        py.display.update()
        clock.tick(60)
    py.quit()


main()

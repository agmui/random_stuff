import pygame as py
import time

# from pygame.locals import *

py.init()
py.display.set_caption('chess')
clock = py.time.Clock()  # FPS stuff
size = 50
GD = py.display.set_mode((size * 8 + 200, size * 8))
crashed = False
select = 0

Bking_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Bking.png')
Bqueen_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Bqueen.png')
Bbishop_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Bbishop.png')
Bknight_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Bknight.png')
Brook_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Brook.png')
Bpawn_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Bpawn.png')
Wking_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Wking.png')
Wqueen_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Wqueen.png')
Wbishop_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Wbishop.png')
Wknight_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Wknight.png')
Wrook_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Wrook.png')
Wpawn_pic = py.image.load(r'C:\Users\antho\Documents\GitHub\random_stuff\chess4D\assets\Wpawn.png')


# Bking_pic = py.image.load('/Users/Anthony/PycharmProjects/random_stuff/chess4D/assets/King.png')  # .convert_alpha()
# Bqueen_pic = py.image.load('/Users/Anthony/PycharmProjects/random_stuff/chess4D/assets/Queen.png')  # .convert_alpha()

# sprite_list = [Bking_pic, Bqueen_pic, Bbishop_pic, Bknight_pic, Brook_pic, Bpawn_pic, Wking_pic, Wqueen_pic,
#               Wbishop_pic, Wknight_pic, Wrook_pic, Wpawn_pic]


class piece:
    def __init__(self, pos, type, img):
        self.pos = pos
        self.color, self.type = type
        self.img = img
        self.size = self.img.get_size()

    def draw(self):
        GD.blit(py.transform.scale(self.img, (size - 5, size - 5)), (self.pos[0] + 3, self.pos[1] + 3))

    def move(self, direction, amount):
        if self.type == 'p':
            pass
        elif self.type == 'k':
            pass
        elif self.type == 'b':
            pass
        elif self.type == 'r':
            if direction[0] == -1:
                self.pos = (self.pos[0], self.pos[1] - 50 * amount[0])
            elif direction[0] == 1:
                self.pos = (self.pos[0], self.pos[1] + 50 * amount[0])
            elif direction[1] == -1:
                self.pos = (self.pos[0] - 50 * amount[1], self.pos[1])
            elif direction[1] == 1:
                self.pos = (self.pos[0] + 50 * amount[1], self.pos[1])
        elif self.type == 'q':
            if direction[0] == -1:
                self.pos = (self.pos[0], self.pos[1] - 50 * amount[0])
            elif direction[0] == 1:
                self.pos = (self.pos[0], self.pos[1] + 50 * amount[0])
            if direction[1] == -1:
                self.pos = (self.pos[0] - 50 * amount[1], self.pos[1])
            elif direction[1] == 1:
                self.pos = (self.pos[0] + 50 * amount[1], self.pos[1])
        elif self.type == 'King':
            if direction[0] == 1:
                self.pos = (self.pos[0] + 50, self.pos[1])
            elif direction[0] == -1:
                self.pos = (self.pos[0] - 50, self.pos[1])
            if direction[1] == 1:
                self.pos = (self.pos[0], self.pos[1] + 50)
            elif direction[1] == -1:
                self.pos = (self.pos[0], self.pos[1] - 50)

    def move_check(self, mx, my):
        direction, amount = [0, 0], [0, 0]
        if self.type == 'p':
            pass
        elif self.type == 'k':
            pass
        elif self.type == 'b':
            pass
        elif self.type == 'r':
            if self.pos[0] <= mx <= self.pos[0] + 50:
                direction[0] = (1 if my >= self.pos[1] else -1)
                amount[0] = abs(int(my / 50) - int(self.pos[1] / 50))
            elif self.pos[1] <= my <= self.pos[1] + 50:
                direction[1] = (1 if mx >= self.pos[0] else -1)
                amount[1] = abs(int(mx / 50) - int(self.pos[0] / 50))
            else:
                return False
            return direction, amount
        elif self.type == 'q':
            if self.pos[0] <= mx <= self.pos[0] + 50:
                direction[0] = (1 if my >= self.pos[1] else -1)
                amount[0] = abs(int(my/50)-int(self.pos[1]/50))
            if self.pos[1] <= my <= self.pos[1] + 50:
                direction[1] = (1 if mx >= self.pos[0] else -1)
                amount[1] = abs(int(mx / 50) - int(self.pos[0] / 50))
            if direction == [0, 0]:
                return False
            return direction, amount
        elif self.type == 'King':
            if abs(int(mx / 50) - int(self.pos[0] / 50)) <= 1 and abs(int(my / 50) - int(self.pos[1] / 50)) <= 1:
                return (int(mx / 50) - int(self.pos[0] / 50), int(my / 50) - int(self.pos[1] / 50)), 1


def init_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                c = (227, 187, 154)
            else:
                c = (201, 123, 58)
            py.draw.rect(GD, c, (j * size, i * size, size, size))
    for pieces_ in p:
        pieces_.draw()


def UI():
    py.draw.rect(GD, (255, 255, 255), (size * 8, 0, 200, size * 8))
    font = py.font.Font('freesansbold.ttf', 32)
    text = font.render('Moves:', True, (0, 0, 0))
    GD.blit(text, (size * 8 + 10, 0))


# set up chess pieces
Bking = piece((size * 4, 0), ('B', 'King'), Bking_pic)
Bqueen = piece((size * 3, 0), ('B', 'q'), Bqueen_pic)
Bbishop1 = piece((size * 2, 0), ('B', 'King'), Bbishop_pic)
Bknight1 = piece((size * 1, 0), ('B', 'King'), Bknight_pic)
Brook1 = piece((size * 0, 0), ('B', 'r'), Brook_pic)
Bbishop2 = piece((size * 5, 0), ('B', 'King'), Bbishop_pic)
Bknight2 = piece((size * 6, 0), ('B', 'King'), Bknight_pic)
Brook2 = piece((size * 7, 0), ('B', 'r'), Brook_pic)
Bpawn1 = piece((size * 0, size * 1), ('B', 'King'), Bpawn_pic)
Wking = piece((size * 4, size * 7), ('W', 'King'), Wking_pic)
Wqueen = piece((size * 3, size * 7), ('W', 'q'), Wqueen_pic)
Wbishop1 = piece((size * 2, size * 7), ('W', 'King'), Wbishop_pic)
Wknight1 = piece((size * 1, size * 7), ('W', 'King'), Wknight_pic)
Wrook1 = piece((size * 0, size * 7), ('W', 'r'), Wrook_pic)
Wbishop2 = piece((size * 5, size * 7), ('W', 'King'), Wbishop_pic)
Wknight2 = piece((size * 6, size * 7), ('W', 'King'), Wknight_pic)
Wrook2 = piece((size * 7, size * 7), ('W', 'r'), Wrook_pic)
Wpawn1 = piece((size * 0, size * 6), ('W', 'King'), Wpawn_pic)

# list of all pieces
p = [Bking, Bqueen, Bbishop1, Bknight1, Brook1, Bbishop2, Bknight2, Brook2, Bpawn1, Wking, Wqueen, Wbishop1, Wknight1,
     Wrook1, Wbishop2, Wknight2, Wrook2, Wpawn1]


def main():
    global py, crashed, size, select
    while not crashed:  # makes window not buggy
        for event in py.event.get():
            if event.type == py.QUIT:
                crashed = True
            elif event.type == py.MOUSEBUTTONDOWN:
                mx, my = py.mouse.get_pos()

                for pieces_ in p:
                    x, y = pieces_.pos
                    if x <= mx <= x + 50 and y <= my <= y + 50:
                        print('on', pieces_.type)
                        select = pieces_
                        break
                    else:
                        #print('off', pieces_.type)
                        if select != 0 and select.move_check(mx, my):  # check if possible pos
                            direction, amount = select.move_check(mx, my)[0], select.move_check(mx, my)[1]
                            print(direction, amount)
                            select.move(select.move_check(mx, my)[0], select.move_check(mx, my)[1])
                            break
                        else:
                            select = 0

                if select != 0:
                    print('selected', select.type)  # ts
                else:
                    print('selected none')
        init_board()
        UI()

        py.display.update()
        clock.tick(60)
    py.quit()


main()
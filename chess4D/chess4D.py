import os
import pygame as py
import time

py.init()
py.display.set_caption('chess')
clock = py.time.Clock()  # FPS stuff
size = 50
GD = py.display.set_mode((size * 8 + 200, size * 8))
crashed = False
select = 0
action = False

Bking_pic = py.image.load(os.path.join("assets", "Bking.png"))
Bqueen_pic = py.image.load(os.path.join("assets", "Bqueen.png"))
Bbishop_pic = py.image.load(os.path.join("assets", "Bbishop.png"))
Bknight_pic = py.image.load(os.path.join("assets", "Bknight.png"))
Brook_pic = py.image.load(os.path.join("assets", "Brook.png"))
Bpawn_pic = py.image.load(os.path.join("assets", "Bpawn.png"))
Wking_pic = py.image.load(os.path.join("assets", "Wking.png"))
Wqueen_pic = py.image.load(os.path.join("assets", "Wqueen.png"))
Wbishop_pic = py.image.load(os.path.join("assets", "Wbishop.png"))
Wknight_pic = py.image.load(os.path.join("assets", "Wknight.png"))
Wrook_pic = py.image.load(os.path.join("assets", "Wrook.png"))
Wpawn_pic = py.image.load(os.path.join("assets", "Wpawn.png"))


class piece:
    def __init__(self, pos, type, img):
        self.pos = pos
        self.color, self.type = type
        self.img = img
        self.size = self.img.get_size()

    def draw(self):
        GD.blit(py.transform.scale(self.img, (size - 17, size - 17)), (self.pos[0] + 8, self.pos[1] + 8))

    def move(self, direction, amount):
        self.pos = (self.pos[0] + size * amount * direction[1], self.pos[1] + size * amount * direction[0])

    def move_check(self, mx, my):
        direction, amount = [0, 0], [0, 0]
        if self.type == 'p':
            direction = abs(int(my / size) - int(self.pos[1] / size)), abs(int(mx / size) - int(self.pos[0] / size))
            if direction[0] == 1 and direction[1] == 0:
                pass
            elif self.type == 'B' and self.pos[1] == 1 and direction[0] == 2 and direction[1] == 0:
                pass
            elif self.type == 'W' and self.pos[1] == 6 and direction[0] == 2 and direction[1] == 0:
                pass
            else:
                return False
            return direction, amount
        elif self.type == 'k':
            try:
                if abs(int(my / size) - int(self.pos[1] / size)) / abs(
                        int(mx / size) - int(self.pos[0] / size)) == 2 or abs(
                    int(my / size) - int(self.pos[1] / size)) / abs(int(mx / size) - int(self.pos[0] / size)) == 1 / 2:
                    direction = int(my / size) - int(self.pos[1] / size), int(mx / size) - int(self.pos[0] / size)
                else:
                    return False
                return direction, 1
            except:
                return False
        elif self.type == 'b':
            if abs(int(my / size) - int(self.pos[1] / size)) == abs(int(mx / size) - int(self.pos[0] / size)):
                direction = ((1 if my >= self.pos[1] else -1), (1 if mx >= self.pos[0] else -1))
                amount = abs(int(my / size) - int(self.pos[1] / size))
            else:
                return False
            return direction, amount
        elif self.type == 'r':
            if self.pos[0] <= mx <= self.pos[0] + size:
                direction = (1 if my >= self.pos[1] else -1), 0
                amount = abs(int(my / size) - int(self.pos[1] / size))
            elif self.pos[1] <= my <= self.pos[1] + size:
                direction = 0, (1 if mx >= self.pos[0] else -1)
                amount = abs(int(mx / size) - int(self.pos[0] / size))
            else:
                return False
            return direction, amount
        elif self.type == 'q':
            if self.pos[0] <= mx <= self.pos[0] + size:  # rook like code
                direction[0] = (1 if my >= self.pos[1] else -1)
                amount = abs(int(my / size) - int(self.pos[1] / size))
            elif self.pos[1] <= my <= self.pos[1] + size:
                direction[1] = (1 if mx >= self.pos[0] else -1)
                amount = abs(int(mx / size) - int(self.pos[0] / size))
            elif abs(int(my / size) - int(self.pos[1] / size)) == abs(
                    int(mx / size) - int(self.pos[0] / size)):  # bishop like code
                direction = ((1 if my >= self.pos[1] else -1), (1 if mx >= self.pos[0] else -1))
                amount = abs(int(my / size) - int(self.pos[1] / size))
            else:
                return False
            return direction, amount
        elif self.type == 'King':
            if abs(int(mx / size) - int(self.pos[0] / size)) <= 1 and abs(
                    int(my / size) - int(self.pos[1] / size)) <= 1:
                return (int(my / size) - int(self.pos[1] / size), int(mx / size) - int(self.pos[0] / size)), 1


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

    font = py.font.Font('freesansbold.ttf', 10)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'uwu lol']
    for i in range(9):
        text = font.render(letters[i], True, (227, 187, 154) if i % 2 == 0 else (201, 123, 58))
        GD.blit(text, (size * i + 40, size * 8 - 10))
        text = font.render(str(i), True, (201, 123, 58) if i % 2 == 0 else (227, 187, 154))
        GD.blit(text, (size - 45, size * (8 - i) + 5))


def UI(action):
    py.draw.rect(GD, (255, 255, 255), (size * 8, 0, 200, size * 8))
    font = py.font.Font('freesansbold.ttf', 32)
    text = font.render('Moves:', True, (0, 0, 0))
    GD.blit(text, (size * 8 + 10, 0))
    if action:
        font = py.font.Font('freesansbold.ttf', 14)
        text = font.render(f"{action[0]}{action[1][0] / 50}{action[1][1] / 50}", True, (0, 0, 0))
        GD.blit(text, (size * 8 + 10, 50))


# set up chess pieces
Bking = piece((size * 4, 0), ('B', 'King'), Bking_pic)
Bqueen = piece((size * 3, 0), ('B', 'q'), Bqueen_pic)
Bbishop1 = piece((size * 2, 0), ('B', 'b'), Bbishop_pic)
Bknight1 = piece((size * 1, 0), ('B', 'k'), Bknight_pic)
Brook1 = piece((size * 0, 0), ('B', 'r'), Brook_pic)
Bbishop2 = piece((size * 5, 0), ('B', 'b'), Bbishop_pic)
Bknight2 = piece((size * 6, 0), ('B', 'k'), Bknight_pic)
Brook2 = piece((size * 7, 0), ('B', 'r'), Brook_pic)
Bpawn1 = piece((size * 0, size * 1), ('B', 'p'), Bpawn_pic)
Wking = piece((size * 4, size * 7), ('W', 'King'), Wking_pic)
Wqueen = piece((size * 3, size * 7), ('W', 'q'), Wqueen_pic)
Wbishop1 = piece((size * 2, size * 7), ('W', 'b'), Wbishop_pic)
Wknight1 = piece((size * 1, size * 7), ('W', 'k'), Wknight_pic)
Wrook1 = piece((size * 0, size * 7), ('W', 'r'), Wrook_pic)
Wbishop2 = piece((size * 5, size * 7), ('W', 'b'), Wbishop_pic)
Wknight2 = piece((size * 6, size * 7), ('W', 'k'), Wknight_pic)
Wrook2 = piece((size * 7, size * 7), ('W', 'r'), Wrook_pic)
Wpawn1 = piece((size * 0, size * 6), ('W', 'p'), Wpawn_pic)

# list of all pieces
p = [Bking, Bqueen, Bbishop1, Bknight1, Brook1, Bbishop2, Bknight2, Brook2, Bpawn1, Wking, Wqueen, Wbishop1, Wknight1,
     Wrook1, Wbishop2, Wknight2, Wrook2, Wpawn1]


def main():
    global py, crashed, size, select, action
    while not crashed:  # makes window not buggy
        for event in py.event.get():
            if event.type == py.QUIT:
                crashed = True
            elif event.type == py.MOUSEBUTTONDOWN:
                mx, my = py.mouse.get_pos()
                found = False
                for pieces_ in p:
                    x, y = pieces_.pos
                    if x <= mx <= x + size and y <= my <= y + size:
                        print('on', pieces_.type)
                        select = pieces_
                        found = True
                        break
                if select != 0 and found == False and select.move_check(mx, my):  # check if possible pos
                    direction, amount = select.move_check(mx, my)[0], select.move_check(mx, my)[1]
                    print(direction, amount)
                    select.move(select.move_check(mx, my)[0], select.move_check(mx, my)[1])
                    print('selected', select.type)
                    action = select.type, select.pos
                elif found:
                    pass
                else:
                    select = 0
                    print('selected none')

        init_board()
        UI(action)

        py.display.update()
        clock.tick(60)
    py.quit()


main()

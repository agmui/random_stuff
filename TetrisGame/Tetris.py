class Block:
    # make 3 rules?
    # -cant go though each other
    # -stays together as one shape
    def __init__(self, x, y):
        self.pos = [x, y]

    def move(self, dir):
        self.pos[0] += dir[0]
        self.pos[1] += dir[1]

    def corner(self, center):
        self.pos = [x+1, y+1]

    def getPos(self):
        return self.pos


def instructions(type):
    if type == 0:  # I block
        return 0, [Block(6, 0), Block(5, 0), Block(4, 0), Block(3, 0)]
    elif type == 1:  # J block
        return 1, [Block(3, 0), Block(5, 1), Block(4, 1), Block(3, 1)]
    elif type == 2:  # L block
        return 2, [Block(), Block(), Block(), Block()]
    elif type == 3:  # O block
        return 3, [Block(), Block(), Block(), Block()]
    elif type == 4:  # S blcok
        return 4, [Block(), Block(), Block(), Block()]
    elif type == 5:  # T block
        return 5, [Block(), Block(), Block(), Block()]
    elif type == 6:  # Z block
        return 6, [Block(), Block(), Block(), Block()]


class Piece:
    def __init__(self, blocks):
        self.blocks = blocks[1]
        self.type = blocks[0]
        self.angle = 0

    def gravity(self):
        self.move([0, 1])

    def move(self, dir):
        if dir != 0:
            past_bigger = 0  # checks the most right or left block to see if it will go though wall
            past_smaller = 9
            for i in self.blocks:  # fix
                if (x := i.getPos()[0]) > past_bigger:
                    past_bigger = x
                    if past_bigger + dir[0] > 9:
                        return
                if x < past_smaller:
                    past_smaller = x
                    if past_smaller + dir[0] < 0:
                        return
            for i in self.blocks:
                i.move(dir)

    def rotate(self):
        if self.type == 0:
            pass
        elif self.type == 1:
           if self.angle == 0:
               self.blocks =

    def getPos(self):
        return [i.getPos() for i in self.blocks]


def init():
    global test
    test = Piece(instructions(1))


count = 0


def main(arrowKeys):
    global count
    # contorls speed of gravity
    if count < 70:  # idk fix
        count += 1
    else:
        count = 0
        test.gravity()
    if arrowKeys != 0:
        if type(arrowKeys) == int:
            test.move([arrowKeys, 0])
        elif arrowKeys == "drop":
            pass
        else:
            test.rotate()


if __name__ == '__main__':
    init()
    main()

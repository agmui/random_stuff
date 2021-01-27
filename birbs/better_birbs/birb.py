birb_list = []


class birb:
    def __init__(self, pos, angle):
        self.pos = pos
        self.angle = angle
        self.speed = 10

    def someMoveFunction(self):#ts
        self.pos = [self.pos[0]+10, self.pos[1]]

    def getPos(self):
        return self.pos


def main():
    for i in range(5):
        b = birb([0, 0], 0)
        birb_list.append(b)


main()

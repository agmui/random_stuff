import math

num_of_birbs = 2
birb_list = []
poslist = []


class birb:
    def __init__(self, pos, angle):
        self.pos = pos
        self.angle = angle
        self.speed = 10
        self.nearByBirbsList = []

    def path_finding(self):
        self.sight()
        self.avoid_filter()
        self.same_direction_filter()
        self.center_dive()
        #self.move()

    def sight(self):
        for i in poslist:
            dx, dy = self.pos[0] - i[0], i[1] - self.pos[1]
            distance = math.hypot(dx, dy)
            angle = math.degrees(math.atan2(dy, dx))*-1
            if 0 != distance <= 100 and not (-90 + 10 >= angle >= -90 - 10):
                self.nearByBirbsList.append([distance, angle])
                #if self.pos == [150, 100]:
                #    print(angle)

    def avoid_filter(self):
        total = 0
        for i in self.nearByBirbsList:
            distance, angle = i[0], i[1]
            total -= math.exp(0.1*distance-1) * angle
        self.angle += total

    def same_direction_filter(self):
        pass

    def center_dive(self):
        pass

    def move(self):
        r = 1
        self.pos[0] += r * math.cos(self.angle)  # make sure it is in radians or something
        self.pos[1] += r * math.sin(self.angle)

    def getPos(self):
        return self.pos

    def getAngle(self):
        return self.angle


def getAllBirbPos():
    poslist.clear()
    for i in birb_list:
        poslist.append(i.getPos())


def init():
    # for i in range(num_of_birbs):
    #    b = birb([0, 0], 0)
    #    birb_list.append(b)
    b1 = birb([100, 100], 0)
    b2 = birb([150, 100], 0)
    birb_list.append(b1)
    birb_list.append(b2)


def main(Mouse_x, Mouse_y):
    if Mouse_x != -1:
        birb_list[0].pos = (Mouse_x, Mouse_y)
    getAllBirbPos()
    for i in birb_list:
        i.path_finding()
        # i.move()


if __name__ == '__main__':
    main()

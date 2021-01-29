import math

num_of_birbs = 2
birb_list = []
poslist = []
"""
     90 
+-180 >  0
    -90
"""

class birb:
    def __init__(self, pos, angle):
        self.pos = pos
        self.angle = math.radians(angle)
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
            dx, dy = i[0] - self.pos[0], self.pos[1] - i[1]
            distance = math.hypot(dx, dy)
            angle = math.degrees(math.atan2(dy, dx))
            if 0 != distance <= 100 and not (-90 + 10 >= angle >= -90 - 10):
                self.nearByBirbsList.append([distance, angle])
                if self.pos == [150, 100]:
                    pass#print(self.angle)
            else:
                self.nearByBirbsList.clear()

    def avoid_filter(self):
        total = 0
        for i in self.nearByBirbsList:
            distance, angle = i[0], i[1]
            total -= math.exp(-0.1 * distance - 1) * 0.01#include angle as parameter to get sign/ dir to turn
            print(total)
        self.rotate(total)
        total = 0

    def same_direction_filter(self):
        pass

    def center_dive(self):
        pass

    def move(self):
        r = 1
        self.pos[0] += r * math.cos(self.angle)  # make sure it is in radians or something
        self.pos[1] += r * math.sin(self.angle)

    def rotate(self, deg):
        if deg + self.angle > math.radians(180):
            self.angle = (deg + self.angle - math.radians(180)) - math.radians(180)
        elif deg + self.angle < -180:
            self.angle = (deg + self.angle + math.radians(180)) + math.radians(180)
        else:
            self.angle += deg

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


def main(Mouse_x, Mouse_y, temp):
    if temp == 1:
        birb_list[1].angle += math.radians(10)
    if temp == -1:
        birb_list[1].angle -= math.radians(10)
    if Mouse_x != -1:
        birb_list[0].pos = (Mouse_x, Mouse_y)
    getAllBirbPos()
    for i in birb_list:
        i.path_finding()


if __name__ == '__main__':
    main()

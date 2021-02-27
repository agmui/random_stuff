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
    def __init__(self, pos, angle, id):
        self.pos = pos
        self.angle = math.radians(angle)
        self.speed = 10
        self.nearByBirbsList = []
        self.id = id

    def path_finding(self):
        self.sight()
        self.avoid_filter()
        self.same_direction_filter()
        self.center_dive()
        self.move()

    def blind_spot(self, angle):  # convret self.angle once for speed
        l = [math.degrees(self.angle) - 160, math.degrees(self.angle) + 160]
        for i in range(2):
            if l[i] > 180:
                l[i] -= 360
            elif l[i] < -180:
                l[i] += 360
        if 10 >= math.degrees(self.angle) >= -10:
            return l[0] >= angle or angle >= l[1]
        return l[0] >= angle >= l[1]

    def sight(self):  # bro fix your rads situation
        self.nearByBirbsList.clear()
        for i in poslist:
            dx, dy = i[0] - self.pos[0], self.pos[1] - i[1]
            distance = math.hypot(dx, dy)
            angle = math.atan2(dy, dx)
            if 0 != distance <= 100 and not self.blind_spot(math.degrees(angle)):
                self.nearByBirbsList.append([distance, angle])

    def avoid_filter(self):
        total = 0
        for i in self.nearByBirbsList:
            distance, angle = i[0], i[1]                    # determina if angle is from left or right side with out angle amount as factor
            total += math.exp(-0.1 * distance - 1) * -angle # angle difreation of where to go dosent work bc 0-180 dosent move
            if self.id == 0:
                print(total, angle)
        self.rotate(total)

    def same_direction_filter(self):
        pass

    def center_dive(self):
        pass

    def move(self):
        r = 1
        self.pos[0] += r * math.cos(self.angle)  # make sure it is in radians or something
        self.pos[1] -= r * math.sin(self.angle)

    def rotate(self, deg):
        if deg + self.angle > math.radians(180):
            self.angle = (deg + self.angle - math.radians(180)) - math.radians(180)
        elif deg + self.angle < math.radians(-180):
            self.angle = (deg + self.angle + math.radians(180)) + math.radians(180)
        else:
            self.angle += deg

    def getPos(self):
        return self.pos

    def getAngle(self):
        return self.angle


def getAllBirbPos():  # maybe remove cuz u can just get pos list form birb_list
    poslist.clear()
    for i in birb_list:
        poslist.append(i.getPos())


def init():
    # for i in range(num_of_birbs):
    #    b = birb([0, 0], 0)
    #    birb_list.append(b)
    b1 = birb([100, 120], 0, 0)
    b2 = birb([250, 100], 180, 1)
    birb_list.append(b1)
    birb_list.append(b2)


mouse = False


def main(Mouse_x, Mouse_y):
    if mouse:
        if Mouse_x != -1:
            birb_list[0].pos = (Mouse_x, Mouse_y)
    getAllBirbPos()
    for i in birb_list:
        i.path_finding()


if __name__ == '__main__':
    main()

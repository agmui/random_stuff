import math
import random

birb_list = []
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

    def blind_spot(self, angle):  # convret self.angle once for speed for blind_spot, sight, and L_or_R
        l = [math.degrees(self.angle) + 160, math.degrees(self.angle) - 160]
        for i in range(2):
            if l[i] > 180:
                l[i] -= 360
            elif l[i] < -180:
                l[i] += 360
        if 10 >= math.degrees(self.angle) >= -10:
            return l[1] >= angle or angle >= l[0]
        return l[1] >= angle >= l[0]

    def sight(self):  # bro fix your rads situation
        self.nearByBirbsList.clear()
        for i in birb_list:
            dx, dy = i.getPos()[0] - self.pos[0], self.pos[1] - i.getPos()[1]
            distance = math.hypot(dx, dy)
            if 0 != distance <= 150 and not self.blind_spot(math.degrees(angle := math.atan2(dy, dx))):
                self.nearByBirbsList.append([distance, angle, i.getAngle()])

    # could check if self == angle and just have it go 50/50
    # make relitive angle a factor
    # make find diffrance function cuz same _ dir uses same function as aVoid_filter
    def L_or_R(self, angle):  # merge dis function with avoid_filter?
        angle = math.degrees(angle)
        angle -= math.degrees(self.angle)
        if angle > 180:
            angle -= 360
        elif angle < -180:
            angle += 360
        return -1 if angle >= 0 else 1

    def avoid_filter(self):
        total = 0
        for i in self.nearByBirbsList:
            distance, angle = i[0], i[1]
            total += 0.055 * math.exp(-0.01 * distance) * self.L_or_R(angle)
        self.rotate(total)

    def same_direction_filter(self):
        for i in self.nearByBirbsList:
            angle = i[2]
            self.rotate(math.radians(-self.L_or_R(angle)))

    def center_dive(self):
        for i in self.nearByBirbsList:
            angle = i[1]
            self.rotate(math.radians(-0.5*self.L_or_R(angle)))


    def move(self):
        r = 3
        self.pos[0] += r * math.cos(self.angle)  # make sure it is in radians or something
        self.pos[1] -= r * math.sin(self.angle)
        if self.getPos()[0] > 800:
            self.pos[0] = 0
        elif self.getPos()[0] < 0:
            self.pos[0] = 800
        if self.getPos()[1] > 690:
            self.pos[1] = 0
        elif self.getPos()[1] < 0:
            self.pos[1] = 690

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


def init():
    global num_of_birbs
    num_of_birbs = 60
    for i in range(num_of_birbs):
        birb_list.append(birb([random.randint(0, 800), random.randint(0, 690)], random.randint(-180, 180), 1))


def ts():
    global num_of_birbs
    num_of_birbs = 2
    b1 = birb([100, 390], 0, 0)
    b2 = birb([251, 400], -180, 1)
    birb_list.append(b1)
    birb_list.append(b2)


def test():
    global num_of_birbs
    num_of_birbs = 12
    b0 = birb([100, 110], 0, 0)
    b1 = birb([300, 100], 180, 1)
    b2 = birb([100, 390], 0, 2)
    b3 = birb([300, 400], 180, 3)
    b4 = birb([600, 100], 0, 4)
    b5 = birb([700, 200], 90, 5)
    b6 = birb([600, 500], 90, 6)
    b7 = birb([700, 400], 180, 7)
    b8 = birb([100, 500], -90, 8)
    b9 = birb([110, 650], 90, 9)
    b10 = birb([310, 500], -90, 10)
    b11 = birb([300, 650], 90, 11)
    birb_list.append(b0)
    birb_list.append(b1)
    birb_list.append(b2)
    birb_list.append(b3)
    birb_list.append(b4)
    birb_list.append(b5)
    birb_list.append(b6)
    birb_list.append(b7)
    birb_list.append(b8)
    birb_list.append(b9)
    birb_list.append(b10)
    birb_list.append(b11)


mouse = False


def main(Mouse_x, Mouse_y):
    if mouse:
        if Mouse_x != -1:
            birb_list[0].pos = (Mouse_x, Mouse_y)
    for i in birb_list:
        i.path_finding()


if __name__ == '__main__':
    ts()
    main(-1, 100)
    # birb_list[0].angle = -1
    print(birb_list[0].L_or_R(math.radians(-10)))

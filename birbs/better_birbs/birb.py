import math
import random

birb_list = []
speed = 5
sight_radius = 300
WINDOW_WIDTH = 1500  # 800
WINDOW_HEIGHT = 1050  # 690
circlePos = 0, 0
filters = [True, True, True, True]

"""
     90 
+-180 >  0
    -90
"""


class birb:
    # add velocity
    # change birb pic to have center in right place
    def __init__(self, pos, angle, id):
        self.pos = pos
        self.angle = angle
        self.speed = 10
        self.nearByBirbsList = []
        self.id = id

    def path_finding(self):
        self.sight()
        if len(self.nearByBirbsList) != 0:
            self.separation() if filters[0] else 0
            self.alignment() if filters[1] else 0
            self.cohesion() if filters[2] else 0
        self.avoid_Walls()
        self.move()

    def sight(self):
        self.nearByBirbsList.clear()
        for i in birb_list:
            dx, dy = i.getPos()[0] - self.pos[0], self.pos[1] - i.getPos()[1]
            distance = math.hypot(dx, dy)
            if 0 != distance <= sight_radius:
                angle = math.atan2(dy, dx)
                l = [self.angle + (8 * math.pi / 9), self.angle - (8 * math.pi / 9)]
                for j in range(2):
                    if l[j] > math.pi:
                        l[j] -= 2 * math.pi
                    elif l[j] < -math.pi:
                        l[j] += 2 * math.pi
                if math.pi / 18 >= self.angle >= -math.pi / 18:
                    test = (l[1] >= angle or angle >= l[0])
                else:
                    test = (l[1] >= angle >= l[0])
                if not test:
                    self.nearByBirbsList.append([distance, angle, i.getAngle(), i.getPos()])

    def L_or_R(self, angle):  # determans if the angle is to the left or right of birb and returns which side it on
        angle = angle - self.angle
        if angle > math.pi:
            angle -= 2 * math.pi
        elif angle < -math.pi:
            angle += 2 * math.pi
        return 1 if angle > 0 else (-1 if angle < 0 else random.choice([1, -1]))

    # remove the rotate funciton to just change angle, then rotate at the very end
    # make relative angle a factor
    def separation(self):
        total = 0
        for i in self.nearByBirbsList:
            distance, angle = i[0], i[1]
            total += 0.1 * math.exp(-0.005 * distance) * -self.L_or_R(angle)
        self.rotate(total)

    def alignment(self):
        for i in self.nearByBirbsList:
            angle = i[2]
            self.rotate(math.radians(self.L_or_R(angle)))

    def cohesion(self):
        global circlePos
        x = sum(i[0] for i in (i[3] for i in self.nearByBirbsList)) / len(self.nearByBirbsList)
        y = sum(i[1] for i in (i[3] for i in self.nearByBirbsList)) / len(self.nearByBirbsList)
        angle = math.atan2(self.pos[1] - y, x - self.pos[0])
        self.rotate(math.radians(6 * self.L_or_R(angle)))
        #if self.id == 0: # fix
        #    circlePos = x, y

    def avoid_Walls(self):
        if self.getPos()[0] > WINDOW_WIDTH - 400:  # right border
            distance = (WINDOW_WIDTH - self.getPos()[0])
            total = math.exp(-0.025 * distance) * math.copysign(1, self.angle)
            self.rotate(total)
        elif self.getPos()[0] < 400:  # left border
            distance = (self.getPos()[0])
            total = math.exp(-0.025 * distance) * math.copysign(1, -self.angle)
            self.rotate(total)
        if self.getPos()[1] > WINDOW_HEIGHT - 400:  # bottom border
            distance = (WINDOW_HEIGHT - self.getPos()[1])
            total = math.exp(-0.015 * distance) * math.copysign(1, -self.L_or_R(-math.pi / 2))
            self.rotate(total)
        elif self.getPos()[1] < 400:  # top border
            distance = (self.getPos()[1])
            total = math.exp(-0.015 * distance) * math.copysign(1, -self.L_or_R(math.pi / 2))
            self.rotate(total)

    def move(self):
        self.pos[0] += speed * math.cos(self.angle)
        self.pos[1] -= speed * math.sin(self.angle)
        if self.getPos()[0] > WINDOW_WIDTH:  # maybe not necessary
            self.pos[0] = 0
        elif self.getPos()[0] < 0:
            self.pos[0] = WINDOW_WIDTH
        if self.getPos()[1] > WINDOW_HEIGHT:
            self.pos[1] = 0
        elif self.getPos()[1] < 0:
            self.pos[1] = WINDOW_HEIGHT

    def rotate(self, deg):
        if deg + self.angle > math.pi:
            self.angle = (deg + self.angle - math.pi) - math.pi
        elif deg + self.angle < -math.pi:
            self.angle = (deg + self.angle + math.pi) + math.pi
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
        birb_list.append(
            birb([random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)], random.randint(-180, 180), 0))


def ts():
    global num_of_birbs
    b1 = birb([500, 460], math.radians(-90), 0)
    # b2 = birb([125, 400], 0, 1)
    # b3 = birb([275, 400], math.radians(0), 2)
    birb_list.append(b1)
    # birb_list.append(b2)
    # birb_list.append(b3)
    num_of_birbs = len(birb_list)


def test():
    global num_of_birbs
    b0 = birb([100, 110], 0, 0)
    b1 = birb([300, 100], math.pi, 1)
    b2 = birb([100, 390], 0, 2)
    b3 = birb([300, 400], math.pi, 3)
    b4 = birb([600, 100], 0, 4)
    b5 = birb([700, 200], math.pi / 2, 5)
    b6 = birb([600, 500], math.pi / 2, 6)
    b7 = birb([700, 400], math.pi, 7)
    b8 = birb([100, 500], -math.pi / 2, 8)
    b9 = birb([110, 650], math.pi / 2, 9)
    b10 = birb([310, 500], -math.pi / 2, 10)
    b11 = birb([300, 650], math.pi / 2, 11)
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
    num_of_birbs = len(birb_list)


mouse = False


def main(Mouse_x, Mouse_y):
    Mouse_x, Mouse_y = Mouse_x, Mouse_y
    if mouse:
        if Mouse_x != -1:
            birb_list[0].pos = (Mouse_x, Mouse_y)
    for i in birb_list:
        i.path_finding()


if __name__ == '__main__':
    ts()
    main(-1, 100)
    print(birb_list[0].L_or_R(math.radians(-10)))

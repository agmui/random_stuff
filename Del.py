import math
import portion as P
import random

"""
def blind_spot(self, angle):  # convret self.angle once for speed for blind_spot, sight, and L_or_R
    l = [math.degrees(self) + 160, math.degrees(self) - 160]
    for i in range(2):
        if l[i] > 180:
            l[i] -= 360
        elif l[i] < -180:
            l[i] += 360
    if 10 >= math.degrees(self) >= -10:
        return l[1] >= angle or angle >= l[0]
    return l[1] >= angle >= l[0]


def L_or_R(self, angle):  # merge dis function with avoid_filter?
    if blind_spot(self, angle):
        return "in blind spot ----------"
    E = [self + 160, self - 160] # dont have to calcuate both E[0] and E[1] cuz we end up using only one
    for i in range(2):
        if E[i] > 180:
            E[i] -= 360
        elif E[i] < -180:
            E[i] += 360
    print(E, end=' ')
    if self >= 0:
        if self <= angle <= 180 or -180 >= angle >= E[0]:  # del "or 180"?
            return -1
        else:  # del later
            return 1
    elif self <= 0:
        if self >= angle >= -180 or E[1] <= angle <= 180 * (-1 if -20 <= self < 0 else 1):  # del "or 180"?
            return 1
        else:
            return -1


print(L_or_R(-20, 180), "should be 1")
print(L_or_R(-19, 180), "should be 1") # help with blind spot code
print(L_or_R(20, -90), "should be 1")

print(L_or_R(-5.8, -1), -1)
print(L_or_R(0, -90), 1)
print(L_or_R(179, -90), -1)
"""
def L_or_R(self, angle):
    angle -= self
    if angle > 180:
        angle -= 360
    elif angle < -180:
        angle += 360
    print(self, angle, end = ' ')
    return -1 if angle >= 0 else 1

print(L_or_R(-176.44657665935395, 172.6680756538965), 1)
#print(L_or_R(20, -90), "should be 1")
#print(L_or_R(50, -90), "should be 1")

def test():
    print(L_or_R(0, 90), -1)  # ans should be +
    print(L_or_R(45, 90), -1)  # ans should be +
    print(L_or_R(90, 91), -1)  # ans should be -
    print(L_or_R(135, 90), 1)  # ans should be -
    print(L_or_R(180, 90), 1)  # ans should be -
    print(L_or_R(-135, 90), 1)  # ans should be -
    print(L_or_R(-90, -180), 1)  # ans should be -
    print(L_or_R(-45, 90), -1)  # ans should be -
    print(L_or_R(-1, 90), -1)
    print(L_or_R(179, 90), 1)
    print(L_or_R(179, -90), -1)
    print(L_or_R(-179, 90), 1)
    print(L_or_R(-179, -90), -1)
    print(L_or_R(20, 90), -1)
    print(L_or_R(-20, 90), -1)
    print(L_or_R(-20, 90), "should be -1")
    print(L_or_R(-.1, 90), "should be -1")
    print(L_or_R(-90, -180), "should be 1")
    print(L_or_R(-90, 180), "should be 1")
    print(L_or_R(-90, -170), "should be 1")
    print(L_or_R(-20, 180), "should be 1")
    print(L_or_R(20, -180), "should be -1")
    print(L_or_R(20, -90), "should be 1")
    print(L_or_R(160, 90), "should be 1")
    print(L_or_R(-160, -90), "should be -1")
    print(L_or_R(-1, -90), 1)
    print(L_or_R(180, -179), -1)

#test()
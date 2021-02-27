import math
import portion as P
import random

def L_or_R(self, angle):  # merge dis function with avoid_filter?
    l = [self + 160, self - 160]
    for i in range(2):
        if l[i] > 180:
            l[i] -= 360
        elif l[i] < -180:
            l[i] += 360
    if self >= 0:
        if self <= angle <= 180 or 180 <= angle <= l[0]:  # del "or 180"?
            return -1
        else:  # del later
            return 1
    elif self <= 0:
        if self <= angle <= 180 or 180 <= angle <= l[1]:  # del "or 180"?
            return 1
        else:
            return -1


#print(L_or_R(-179.99894668465197, -168.1113408682082))
print(random.randint(8, 6))
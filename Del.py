import math


def differenceAngle(self, angle):  # returns the difference angle between two birbs
    angle = angle - self
    if angle > math.pi:
        angle -= 2 * math.pi
    elif angle < -math.pi:
        angle += 2 * math.pi
    return angle


angle = -2.9
x = (1/(differenceAngle(-math.pi, angle)*5))
print(math.degrees(x))

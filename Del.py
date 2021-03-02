def L_or_R(self, angle):
    angle -= self
    if angle > 180:
        angle -= 360
    elif angle < -180:
        angle += 360
    print(self, angle, end = ' ')
    return -1 if angle >= 0 else 1

#print(L_or_R(-176.44657665935395, 172.6680756538965), 1)
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



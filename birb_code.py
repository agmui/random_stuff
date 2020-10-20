import pygame
import time
import random
import math

white = (255, 255, 255)
display_width, display_height = 800, 600
GD = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()  # FPS stuff
birbs = []#[[50, 50, 0], [200, 50, 180], [400, 400, 0], [500, 500, 270]]
number_of_birbs = 50
for i in range(number_of_birbs):  # random spawn of birbs
    birbs.append([random.randint(0, display_width), random.randint(0, display_height), random.randint(0, 360)])
birbs_check = [(-1, -1, -1) for i in range(len(birbs) - 1)]
r = 3.5  # the speed of the birbs
sight_radius = 87  # how far in front they can see

birb = pygame.image.load(r'C:\Users\antho\Desktop\pyImages\birb.png')
green_birb = pygame.image.load(r'C:\Users\antho\Desktop\pyImages\birb_touch.png')
sight = pygame.image.load(r'C:\Users\antho\Desktop\pyImages\sight.png')


class Draw:
    def __init__(self, pic):
        self.pic = pic

    def draw(self, data):
        x, y, deg = data
        img_copy = pygame.transform.rotate(self.pic, -deg)
        GD.blit(img_copy, (x - int(img_copy.get_width() / 2), y - int(img_copy.get_height() / 2)))

    def line(self, color, point1, deg):
        deg = math.radians(deg)
        point2 = 100 * math.cos(deg) + point1[0], 100 * math.sin(deg) + point1[1]
        pygame.draw.line(GD, color, point1, point2)


def wall(x, y):
    if x >= display_width:
        x = 0
    elif x <= 0:
        x = display_width
    if y >= display_height:
        y = 0
    elif y <= 0:
        y = display_height
    return x, y


def events(pause):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return not pause
    return pause


def collision(birbs, x2, y2, j):
    # view_angle is the deg of the other birbs relitive to this birb
    # deg should be what angle the second birb is at relitive to the og birb
    x1, y1, deg = birbs
    distance = math.hypot(x1 - x2, y1 - y2)
    if distance > sight_radius:
        return -1, -1, -1
    else:
        deg += 180
        if deg > 360:
            deg -= 360
        view_angle = math.atan2(y1 - y2, x1 - x2) * (180 / math.pi) + 180
        if deg - 20 < view_angle < deg + 20:
            return -1, -1, -1
        elif 340 < deg <= 360 or 0 <= deg < 20:
            if 340 < view_angle <= 360 or 0 <= view_angle < 20:
                return -1, -1, -1
            else:
                return view_angle, distance, j
        else:
            return view_angle, distance, j


def path_finding(x, y, deg, data, i2):  # rly buggy
    # the radius or distance traveled every step
    # the move code
    final_angle = 0
    y, x = y + math.sin(deg * (math.pi / 180)) * r, x + math.cos(deg * (math.pi / 180)) * r
    if data != birbs_check:
        angle, distance, which_birb = [data[i][0] for i in range(len(data))], [data[i][1] for i in range(len(data))], [
            data[i][2] for i in range(len(data))]
        # the filters--------------------------------------------------
        final_angle = avoid_filter(angle, distance, deg)
        final_angle = same_direction_filter(which_birb, deg, final_angle, i2)
        final_angle = center_dive(angle, distance, deg, final_angle)
        # --------------------------------------------------------------
    if deg + final_angle > 360:  # accounts for when it spins past 0 or 360 for reset
        return x, y, deg + final_angle - 360
    if deg + final_angle < 0:
        return x, y, deg + final_angle + 360
    return x, y, deg + final_angle


def avoid_filter(angle, distance, deg):  # still some bugs like when birbs meet at 90 deg
    final_angle = 0
    for i in range(len(angle)):
        if angle[i] != -1:
            if deg - angle[i] >= 160:  # something wrong with deg
                print(deg - angle[i])
            if deg - angle[i] >= 160:  # for watching the jump from 0 to 360
                turn_angle = deg - angle[i] - 360
                print()
            elif angle[i] - deg >= 160:  # for watching the jump from 0 to 360
                turn_angle = 360 - angle[i] - deg
            else:  # what probs happens most of the time
                turn_angle = deg - angle[i] + 10
            """if turn_angle >= 160:
                turn_angle = 160"""
            # turn_angle is all the angle measurement of one birb relative to all the other birbs position
            final_angle += turn_angle * ((1 / (distance[i] + 1)) - 0.007246)
            # * (0.000053 * ((distance[i] - sight_radius) ** 2))
            # * 2 ** (-0.1 * distance[i])
            # * ((-1 * distance[i] / sight_radius) + 1)
    return final_angle


# finds diff between two angles watching the 0, 360 jump
def diffrence_function(check_angle, deg):  # plz make better
    if deg - check_angle >= 160:  # for watching the jump from 0 to 360
        turn_angle = deg - check_angle - 360
    elif check_angle - deg >= 160:  # for watching the jump from 0 to 360
        turn_angle = 360 - check_angle - deg
    else:  # what probs happens most of the time
        turn_angle = deg - check_angle
    return turn_angle


def same_direction_filter(which_birb, deg, final_angle, i2):
    # "check_angle" is birb2's angle or direction it is facing
    for i in range(len(which_birb)):
        if which_birb[i] != -1:
            check_angle = birbs[which_birb[i]][2]
            # 0.016861 replace .004644 ts
            influence_function = 3.1 ** (0.016861 * abs(diffrence_function(check_angle, deg)) - 0.4) - 0.3636
            # might have problem with difference function
            if check_angle == deg:
                return final_angle
            elif deg > 180:  # to account for 0, 360 jump
                if deg < check_angle < 360 or 0 < check_angle < deg - 180:  # to watch for the 0, 360 gap
                    final_angle += 1 * influence_function
                else:
                    final_angle -= 1 * influence_function
            elif deg < check_angle < deg + 180:  # turn right
                final_angle += 1 * influence_function
            else:  # turn left
                final_angle -= 1 * influence_function
    return final_angle


def center_dive(angle, distance, deg, final_angle):  # error with 0, 360 line
    # distance.sort()
    # distance[:] = [x for x in distance if x != -1]
    x = distance.index(min(distance))
    if angle[x] > deg:
        final_angle += 1 * (3.13035 * (2 ** (0.00801 * angle[x])) - 3.13035)
    elif angle[distance.index(min(distance))] < deg:
        final_angle -= 1 * (3.13035 * (2 ** (0.00801 * angle[x])) - 3.13035)
    else:
        return final_angle
    return final_angle

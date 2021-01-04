import math
import os
import time

import pygame as py

py.init()
py.display.set_caption('LM game')
clock = py.time.Clock()  # FPS stuff
display_width = 1800
display_height = 1000
GD = py.display.set_mode((display_width, display_height))
GD = py.display.set_mode((0, 0), py.RESIZABLE)
crashed = False
fire = False
t = 1 / 60
thrust = 20
grav = 8.8


class Player:
    def __init__(self, fuel):
        self.angle = 180
        self.v = [130, 0]
        self.acc = [0, grav]  # has to be not negative cuz py window
        self.scale = .035
        self.fuel = fuel
        self.image = py.image.load(os.path.join("assets", "LM.png"))
        self.scaled_img = py.transform.rotozoom(self.image, self.angle - 90, self.scale)
        self.mask = py.mask.from_surface(self.image).scale((self.scaled_img.get_width(), self.scaled_img.get_height()))
        self.pos = [100 - self.scaled_img.get_width() / 2, 150 - self.scaled_img.get_height() / 2]
        self.rect = [self.pos[0], self.pos[1], 0, 0]

    def draw(self, fire_):
        self.scaled_img = py.transform.rotozoom(self.image, self.angle - 90, self.scale)
        GD.blit(self.scaled_img,
                (self.pos[0] - self.scaled_img.get_width() / 2, self.pos[1] - self.scaled_img.get_height() / 2))
        if fire_:
            py.draw.rect(GD, (255, 0, 0), py.Rect(self.pos[0] - 10, self.pos[1] + 10, 20, 20))

    def tilt(self, x):
        self.angle += x
        if self.angle > 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360

    def physics(self):
        for i in range(2):
            self.v[i] = self.v[i] + self.acc[i] * t
            self.pos[i] = self.pos[i] + self.v[i] * t + 0.5 * self.acc[i] * t ** 2

    def rocket(self):
        self.acc[0] = thrust * math.cos(self.angle * (math.pi / 180))
        self.acc[1] = grav - thrust * math.sin(self.angle * (math.pi / 180))

    def landed(self):
        self.v = [self.v[0] / 2, 0]
        self.acc = [self.acc[0] / 2, 0]
        level_end()


class Level:
    def __init__(self):
        self.scale = 1
        self.image = py.image.load(os.path.join("assets", "stage.png"))
        self.scaled_img = py.transform.rotozoom(self.image, 0, self.scale)
        self.mask = py.mask.from_surface(self.image).scale((self.scaled_img.get_width(), self.scaled_img.get_height()))
        self.pos = 0, GD.get_height() - self.image.get_height() * self.scale
        self.scroll = 0
        self.rect = py.Rect(self.pos, (self.scaled_img.get_width(), self.scaled_img.get_height()))

    def draw_stage(self, offset):
        for i in range(2):
            # GD.blit(self.scaled_img, (self.pos[0] + i * self.image.get_width(), self.pos[1]))
            GD.blit(self.scaled_img, offset(self.scaled_img))

    def stage_scroll(self):
        pass


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = py.Rect(0, 0, width, height)

    def apply(self, target):
        print(self.state.topleft)
        return self.state.topleft

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect  # l = left,  t = top
    _, _, w, h = camera  # w = width, h = height
    return py.Rect(-l + display_width / 2, -t + display_height / 2, w, h)


def level_end():
    pass


player = Player(100)
level = Level()
camera = Camera(simple_camera, level.scaled_img.get_width(), level.scaled_img.get_height())


def main():
    global crashed, fire
    while not crashed:  # makes window not buggy
        for event in py.event.get():
            if event.type == py.QUIT:
                crashed = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                player.tilt(2)
            elif event.key == py.K_RIGHT:
                player.tilt(-2)
            if event.key == py.K_UP:
                fire = True
        if event.type == py.KEYUP:
            if event.key == py.K_UP:
                player.acc = [0, grav]
                fire = False

        GD.fill((0, 0, 0))  # draw background

        offset = int(player.pos[0] - level.pos[0]), int(player.pos[1] - level.pos[1])
        if level.mask.overlap(player.mask, offset) is not None:
            player.landed()
            GD.fill((155, 155, 155))

        camera.update(player)  # camera follows player. Note that we could also follow any other sprite
        level.draw_stage(camera.apply)
        player.physics()
        # player.pos = py.mouse.get_pos()
        player.draw(fire)
        if fire:
            player.rocket()

        # time.sleep(0.5)
        py.display.update()
        clock.tick(60)
    py.quit()


main()

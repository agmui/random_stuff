"""
tip on rotattion:
have the return function:
py.transform.rotate(self.ogi, self.angle - 90)
not return to the og img

also
rect/pos must be updated after rotation
"""

import math
import os
import pygame as py

py.init()
clock = py.time.Clock()  # FPS stuff
display_width = 200
display_height = 200
GD = py.display.set_mode((display_width, display_height))
crashed = False
#green_alien = r'/Users/Anthony/PycharmProjects/random_stuff/birbs/better_birbs/assets/birb.png'
green_alien = r'C:\Users\antho\Documents\GitHub\random_stuff\birbs\better_birbs\assets\birb.png'


class Player(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.angle = 180
        self.ogi = py.image.load(green_alien)
        self.image = self.ogi# py.image.load(green_alien)
        self.mask = py.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(100, 100))

    def rotate(self, x):
        self.angle += x
        if self.angle > 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360
        self.image = py.transform.rotate(self.ogi, self.angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)


p1 = Player()
sprite_group = py.sprite.Group()
sprite_group.add(p1)


while not crashed:
    for event in py.event.get():
        if event.type == py.QUIT:
            crashed = True

    p1.rotate(10)
    # player.angle = 0
    GD.fill((0, 0, 0))
    sprite_group.draw(GD)

    py.display.update()
    clock.tick(60)
py.quit()
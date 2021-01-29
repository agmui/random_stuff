import math
import os
import pygame as py

py.init()
clock = py.time.Clock()  # FPS stuff
display_width = 200
display_height = 200
GD = py.display.set_mode((display_width, display_height))
crashed = False
green_alien = r'/Users/Anthony/PycharmProjects/random_stuff/birbs/better_birbs/assets/birb.png'


class Player(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.angle = 180
        self.image = py.image.load(green_alien)
        self.mask = py.mask.from_surface(self.image)
        self.pos = [100 - self.image.get_width() / 2, 150 - self.image.get_height() / 2]

    def draw(self):
        image = py.transform.rotate(self.image, self.angle - 90)
        # GD.blit(self.scaled_img,
        #        (self.pos[0] - self.scaled_img.get_width() / 2, self.pos[1] - self.scaled_img.get_height() / 2))
        GD.blit(image, (100, 100))

    def rotate(self, x):
        self.angle += x
        if self.angle > 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360


player = Player()

while not crashed:
    for event in py.event.get():
        if event.type == py.QUIT:
            crashed = True

    player.rotate(1)
    GD.fill((0, 0, 0))
    player.pos = 100, 100
    player.draw()

    py.display.update()
    clock.tick(60)
py.quit()

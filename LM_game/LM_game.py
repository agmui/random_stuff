import math
import os
import pygame as py

py.init()
py.display.set_caption('LM game')
clock = py.time.Clock()  # FPS stuff
GD = py.display.set_mode((1800, 1000))
crashed = False
fire = False
t = 1 / 60
thrust = 20


class Player:  # (py.sprite.Sprite):
    def __init__(self, fuel):
        # py.sprite.Sprite.__init__(self)
        self.pos = [100, 100]
        self.angle = 90
        self.v = [0, 100]  # ts
        self.acc = [0, 9.81]  # has to be not negative cuz py window
        self.fuel = fuel
        self.image = py.image.load(os.path.join("assets", "LM.png"))
        self.mask = py.mask.from_surface(self.image)
        # self.img_player_rect = self.image.get_rect()
        # self.img_player_rect.topleft = (self.pos[0], self.pos[1])
        # self.rect = self.image.get_rect(center=(self.pos[0], self.pos[1]))

    def draw(self, fire_, scale=0.035):
        img = py.transform.rotozoom(self.image, self.angle - 90, scale)
        GD.blit(img, (self.pos[0] - img.get_width() / 2, self.pos[1] - img.get_height() / 2))
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
        self.acc[1] = 9.81 - thrust * math.sin(self.angle * (math.pi / 180))

    def landed(self):
        self.v = [self.v[0] / 2, 0]
        self.acc = [self.acc[0] / 2, 0]


class Level:  # (py.sprite.Sprite):
    def __init__(self):
        # py.sprite.Sprite.__init__(self)
        self.scale = 0.7
        self.image = py.image.load(os.path.join("assets", "stage.png"))
        self.mask = py.mask.from_surface(self.image)
        self.pos = 0, GD.get_height() - self.image.get_height() * self.scale
        # self.img_stage_rect = self.image.get_rect()
        # self.img_stage_rect.topleft = (0, self.pos[1])
        # self.rect = self.image.get_rect(topleft=(0, 102))

    def draw_stage(self):
        img = py.transform.rotozoom(self.image, 0, self.scale)
        GD.blit(img, self.pos)
        #GD.blit(self.image, self.pos)


player = Player(100)
level = Level()

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
                player.pos[1] -= 1  # ts _______________________________________________
            if event.key == py.K_DOWN:
                fire = True
                player.pos[1] += 1
        if event.type == py.KEYUP:
            if event.key == py.K_UP:
                player.acc = [0, 9.81]
                fire = False
            if event.key == py.K_DOWN:
                player.acc = [0, 9.81]
                fire = False

        GD.fill((0, 0, 0))  # draw background

        # if py.sprite.spritecollide(level, group, False, collided=py.sprite.collide_mask):
        offset = int(player.pos[0] - level.pos[0]), int(player.pos[1] - level.pos[1])
        if level.mask.overlap(player.mask, offset) is not None:
            player.landed()
            GD.fill((155, 155, 155))

        level.draw_stage()
        player.physics()
        player.draw(fire)
        if fire:
            player.rocket()

        py.display.update()
        clock.tick(60)
    py.quit()


main()

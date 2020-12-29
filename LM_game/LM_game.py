import math
import os
import pygame as py

py.init()
py.display.set_caption('LM game')
clock = py.time.Clock()  # FPS stuff
GD = py.display.set_mode((500, 500))
crashed = False
fire = False
t = 1 / 60
thrust = 20

LM = py.image.load(os.path.join("assets", "LM.png"))


class Player:
    def __init__(self, fuel):
        self.pos = [100, 100]
        self.angle = 90
        self.v = [0, 0]
        self.acc = [0, 9.81]# has to be not negative cuz py window
        self.fuel = fuel
        self.LM = LM

    def draw(self, fire_, scale=0.2):
        img = py.transform.rotozoom(self.LM, self.angle - 90, scale)
        GD.blit(img, (self.pos[0] - int(img.get_width() / 2), self.pos[1] - int(img.get_height() / 2)))
        if fire_:
            py.draw.rect(GD, (255, 0, 0), py.Rect(self.pos[0]-10, self.pos[1]+10, 20, 20))

    def tilt(self, x):
        self.angle += x

    def physics(self):
        for i in range(2):
            self.v[i] = self.v[i] + self.acc[i] * t
            self.pos[i] = self.pos[i] + self.v[i] * t + 0.5 * self.acc[i] * t ** 2

    def rocket(self):
        self.acc[0] = -thrust*math.cos(self.angle*(math.pi/180))
        self.acc[1] = 9.81-thrust*math.sin(self.angle*(math.pi/180))


player = Player(100)


def main():
    global crashed, fire
    while not crashed:  # makes window not buggy
        for event in py.event.get():
            if event.type == py.QUIT:
                crashed = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                player.tilt(1)
            elif event.key == py.K_RIGHT:
                player.tilt(-1)
            elif event.key == py.K_DOWN:
                player.rocket()
                fire = True
        if event.type == py.KEYUP:
            if event.key == py.K_DOWN:
                player.acc = [0, 9.81]
                fire = False


        GD.fill((255, 255, 255))  # draw background

        player.physics()
        player.draw(fire)

        py.display.update()
        clock.tick(60)
    py.quit()


main()

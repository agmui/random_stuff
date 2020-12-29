import os
import pygame as py

py.init()
py.display.set_caption('LM game')
clock = py.time.Clock()  # FPS stuff
GD = py.display.set_mode((500, 500))
crashed = False

LM = py.image.load(os.path.join("assets", "LM.png"))


class Player:
    def __init__(self, fuel):
        self.pos = [0, 0]
        self.angle = 0
        self.v = 0
        self.acc = [0, 0]
        self.fuel = fuel
        self.LM = LM

    def draw(self):
        img_copy = py.transform.rotate(self.LM, - self.angle)
        GD.blit(img_copy, (self.pos[0] - int(img_copy.get_width() / 2), self.pos[1] - int(img_copy.get_height() / 2)))
        # GD.blit(py.transform.scale(LM, (size, size)), (self.pos[0], self.pos[1]))

    def math(self):
        pass

    def tilt(self, x):
        self.angle += x

player = Player(100)

def main():
    global crashed
    while not crashed:  # makes window not buggy
        for event in py.event.get():
            if event.type == py.QUIT:
                crashed = True
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    player.tilt(10)
                elif event.key == py.K_RIGHT:
                    player.tilt(-10)
                elif event.key == py.K_DOWN:
                    pass

        GD.fill((255, 255, 255))  # draw background

        player.draw()

        py.display.update()
        clock.tick(60)
    py.quit()


main()

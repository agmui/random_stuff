import math
import os
import time

import pygame
from birbs.better_birbs import birb

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 690
num_of_birbs = birb.num_of_birbs
viswals = False

birb_pic = os.path.join("assets", "birb.png")
birb_touch = os.path.join("assets", "birb_touch.png")
sight = os.path.join("assets", "sight.png")


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pic, index):
        pygame.sprite.Sprite.__init__(self)
        self.ogImg = pygame.image.load(pic).convert_alpha()
        self.image = self.ogImg
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(0, 0))
        self.index = index

    def changeColor(self):
        self.image = pygame.image.load(birb_touch).convert_alpha()

    def moveBy(self, changeInPos):
        distance = changeInPos[self.index][0] - self.getPos()[0], changeInPos[self.index][1] - self.getPos()[1]
        self.rect.move_ip(distance)

    def rotate(self, birbList):
        deg = math.degrees(birbList[self.index].getAngle())
        self.image = pygame.transform.rotate(self.ogImg, deg)
        self.rect = self.image.get_rect(center=self.rect.center)

    def getPos(self):
        return self.rect.center


def moveAllBirbs(changeInPos):
    for i in sprite_group:
        i.moveBy(changeInPos)
        if viswals:
            for j in sight_group:
                j.moveBy(changeInPos)
        i.rotate(birb.birb_list)


birb.init()
pygame.init()
pygame.font.init()
SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), SURFACE)

sprite_group = pygame.sprite.Group()  # All sprites for updating and drawing
sight_group = pygame.sprite.Group()
for i in range(num_of_birbs):
    b = Sprite(birb_pic, i)
    sprite_group.add(b)
    if viswals:
        s = Sprite(sight, i)
        sight_group.add(s)

clock = pygame.time.Clock()
done = False
temp = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                temp = -1
            elif event.key == pygame.K_RIGHT:
                temp = 1

    Mouse_x, Mouse_y = pygame.mouse.get_pos()

    birb.main(Mouse_x, Mouse_y)
    changeInPos = birb.poslist
    moveAllBirbs(changeInPos)

    # Repaint the screen
    sprite_group.update()  # re-position the game sprites
    if viswals:
        sight_group.update()
    window.fill((100, 100, 100))

    sprite_group.draw(window)  # draw the game sprites

    if viswals:  # somehow order sight to back--------------------------------------------
        sight_group.draw(window)

    pygame.display.flip()
    clock.tick_busy_loop(60)
    time.sleep(0.1)

pygame.quit()

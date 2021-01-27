# use dis as example
# research about python box2d
# rect function for pos and size
# imports image in classes
import os

import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 690

birb = os.path.join("assets", "temp_birb.png")


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x=50, y=50, idNum=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(birb).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))
        self.newPos = birb.birb_list[idNum]

    def moveBy(self, distance):
        self.rect.move_ip(distance)

    def getPos(self):
        return self.rect.center

    def getNewPos(self):
        return self.newPos

### MAIN
pygame.init()
pygame.font.init()
SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), SURFACE)



sprite_group = pygame.sprite.Group()  # All sprites for updating and drawing
for i in range(5):
    b = Sprite(0, 0, i)
    sprite_group.add(b)

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for i in sprite_group:
        i.moveBy((i.getNewPos[0] - i.getPos()[0], i.getNewPos[1] - i.getPos()[1])) # birb.py file input

    # Repaint the screen
    sprite_group.update()  # re-position the game sprites
    window.fill((100, 100, 100))
    sprite_group.draw(window)  # draw the game sprites

    pygame.display.flip()
    clock.tick_busy_loop(60)

pygame.quit()

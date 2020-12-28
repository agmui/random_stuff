class myc:
    def __init__(self):
        self.x = 0
    def add(self,y):
        self.x += y

import pygame

pygame.init()
clock = pygame.time.Clock()  # FPS stuff
GD = pygame.display.set_mode((50, 50))
crashed = False
hi = False
while not crashed:  # makes window not buggy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                n.add(2)
                hi = True
                print(n.x)
        GD.fill((110, 110, 110))  # draw background
        n = myc()
        if hi:
            n.add(10)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
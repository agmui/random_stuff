#!/usr/bin/env python3

print("hello world")

import pygame

pygame.init()
GD = pygame.display.set_mode((100,100))
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        GD.fill((100,100,100))

    pygame.display.update()

pygame.quit()


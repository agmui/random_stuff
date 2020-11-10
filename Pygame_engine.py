import pygame

pygame.init()
clock = pygame.time.Clock()  # FPS stuff
GD = pygame.display.set_mode((200 * 5, 200 * 5))
crashed = False




while not crashed:  # makes window not buggy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        GD.fill((110, 110, 110))  # draw background

        """
        
        code
        fav colors (50, 50, 50), (250, 250, 250), (110, 110, 110)
        """


    pygame.display.update()
    clock.tick(60)

pygame.quit()
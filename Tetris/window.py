import pygame

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 690
FPS = 60

# background colours
INKY_BLACK = (0, 0, 0)
FIREY_RED = (203, 49, 7)


class Gui(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0, 0))


class Piece(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.altImg = self.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(0, 0))
        self.rotation = 0



### MAIN
pygame.init()
pygame.font.init()
SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), SURFACE)
pygame.display.set_caption("Maze Sprite-Collision Example")



sprite_group = pygame.sprite.Group()  # All sprites for updating and drawing
sprite_group.add(maze)
sprite_group.add(alien)
alien_group = pygame.sprite.GroupSingle()  # Just for the alien collisions
alien_group.add(alien)

clock = pygame.time.Clock()
done = False
while not done:

    # Handle user-input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # make so it can Handle continuous-keypresses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        alien.moveBy(0, -1)
    elif keys[pygame.K_DOWN]:
        alien.moveBy(0, 1)
    elif keys[pygame.K_LEFT]:
        alien.moveBy(-1, 0)
    elif keys[pygame.K_RIGHT]:
        alien.moveBy(1, 0)


    # Repaint the screen
    sprite_group.update()  # re-position the game sprites
    window.fill(background)
    sprite_group.draw(window)  # draw the game sprites

    pygame.display.flip()
    clock.tick_busy_loop(FPS)

pygame.quit()

import os
import pygame
import TetrisGame.Tetris as Tetris

size = 50
# Window size
WINDOW_WIDTH = 10 * size
WINDOW_HEIGHT = 20 * size

# assets
block = os.path.join("assets", "block.png")


class Gui(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0, 0))

    @staticmethod
    def drawLines():
        for i in range(10):
            pygame.draw.line(window, (0, 0, 0), (50 * i, 0), (50 * i, WINDOW_HEIGHT), 1)
        for i in range(20):
            pygame.draw.line(window, (0, 0, 0), (0, 50 * i), (WINDOW_WIDTH, 50 * i), 1)


class SpriteBlock(pygame.sprite.Sprite):
    def __init__(self, image, type=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.altImg = self.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(0, 0))
        self.rotation = 0
        self.type = type

    def moveTo(self, dir):
        self.rect.left = dir[0] * size
        self.rect.top = dir[1] * size


### MAIN
pygame.init()
pygame.font.init()
SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), SURFACE)
pygame.display.set_caption("TetrisGame")

Tetris.init()
sprite_group = pygame.sprite.Group()  # All sprites for updating and drawing
for i in Tetris.test.getPos():
    testPeice = SpriteBlock(block)
    sprite_group.add(testPeice)
    testPeice.moveTo(i)

clock = pygame.time.Clock()
done = False
past = 0
while not done:
    arrowKeys = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # make so it can Handle continuous-keypresses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_x]:
        pygame.quit()
    if keys[pygame.K_UP]:
        arrowKeys = "rotate"
    elif keys[pygame.K_DOWN]:
        arrowKeys = "drop"
    elif keys[pygame.K_LEFT]:
        arrowKeys = -1
    elif keys[pygame.K_RIGHT]:
        arrowKeys = 1

    Tetris.main(arrowKeys)
    for i, block in enumerate(sprite_group):
        block.moveTo(Tetris.test.getPos()[i])

    # Repaint the screen
    sprite_group.update()  # re-position the game sprites
    window.fill((100, 100, 100))
    Gui.drawLines()
    sprite_group.draw(window)  # draw the game sprites

    pygame.display.flip()
    clock.tick_busy_loop(60)

pygame.quit()

"""
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

        #fav colors (50, 50, 50), (250, 250, 250), (110, 110, 110)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
# use dis as example
# reasearch about python box2d ____________________________________________________<---look here use bot code
# rect function for pos and size
# imports image in classes
"""
import pygame

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 690
FPS = 60

# background colours
INKY_BLACK = (0, 0, 0)
FIREY_RED = (203, 49, 7)


class MazeSprite(pygame.sprite.Sprite):
    # A maze with a transparent background as a *huge* sprite 
    def __init__(self, maze_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(maze_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0, 0))


class AlienSprite(pygame.sprite.Sprite):
    # A tiny little alien hoardette
    def __init__(self, alien_image, x=50, y=50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(alien_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))

    def moveBy(self, dx, dy):
        self.rect.move_ip(dx, dy)
        print("Now at %s" % ( str( self.rect.center ) ) )


### MAIN
pygame.init()
pygame.font.init()
SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), SURFACE)
pygame.display.set_caption("Maze Sprite-Collision Example")

# Make some sprites to hold the Maze background and Player's Alien

hexmaze = (r'C:\Users\antho\Documents\GitHub\random_stuff\pygame_exsamples\assets\hexmaze.png')#os.path.join("assets", "hexmaze.png")
maze = MazeSprite(hexmaze)
green_alien = (r'C:\Users\antho\Documents\GitHub\random_stuff\pygame_exsamples\assets\green_alien.png')#os.path.join("assets", "green_alien.png")
alien = AlienSprite(green_alien, 283, 155)

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

    # Handle continuous-keypresses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        alien.moveBy(0, -1)
    elif keys[pygame.K_DOWN]:
        alien.moveBy(0, 1)
    elif keys[pygame.K_LEFT]:
        alien.moveBy(-1, 0)
    elif keys[pygame.K_RIGHT]:
        alien.moveBy(1, 0)

    # has the alien hit the walls?
    background = INKY_BLACK
    # NOTE: Ensure we use "mask" collision
    #       It's not used (here) automatically
    if pygame.sprite.spritecollide(maze, alien_group, False, collided=pygame.sprite.collide_mask):
        # returned list is not empty
        background = FIREY_RED

    # Repaint the screen
    sprite_group.update()  # re-position the game sprites
    window.fill(background)
    sprite_group.draw(window)  # draw the game sprites

    pygame.display.flip()
    clock.tick_busy_loop(FPS)

pygame.quit()

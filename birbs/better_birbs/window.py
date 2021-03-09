import math
import os
import time

import pygame
from birbs.better_birbs import birb

WINDOW_WIDTH = birb.WINDOW_WIDTH
WINDOW_HEIGHT = birb.WINDOW_HEIGHT
viswals = False

birb_pic = os.path.join("assets", "birb2.png")
birb_touch = os.path.join("assets", "birb_touch2.png")
sight = os.path.join("assets", "sight.png")
circle = os.path.join("assets", "circle.png")
pressed_button = os.path.join("assets", "pressed_button.png")
unpressed_button = os.path.join("assets", "unpressed_button.png")
pause = os.path.join("assets", "pause.png")
play = os.path.join("assets", "play.png")
step = os.path.join("assets", "step.png")


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pic, index=0):
        pygame.sprite.Sprite.__init__(self)
        if isinstance(pic, pygame.Surface):
            self.ogImg = pic
        else:
            self.ogImg = pygame.image.load(pic).convert_alpha()
        self.image = self.ogImg
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(0, 0))
        self.index = index

    def changeColor(self):
        self.image = pygame.image.load(birb_touch).convert_alpha()

    def moveBy(self, changeInPos):
        distance = changeInPos[self.index].getPos()[0] - self.getPos()[0], changeInPos[self.index].getPos()[1] - \
                   self.getPos()[1]
        self.rect.move_ip(distance)

    def rotate(self, birbList):
        deg = math.degrees(birbList[self.index].getAngle())
        self.image = pygame.transform.rotate(self.ogImg, deg)
        self.rect = self.image.get_rect(center=self.rect.center)

    def getPos(self):
        return self.rect.center


class Gui(pygame.sprite.Sprite):
    def __init__(self, image, altImg, scale, position, text='', textPos=(45, 5)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), scale)
        self.altImg = pygame.transform.scale(pygame.image.load(altImg), scale) if altImg != False else 0
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=position)
        if text != '':
            self.font = pygame.font.SysFont("Arial", 20, bold=True)
            self.textSurface = self.font.render(text, True, (255, 255, 255))
            self.textRect = self.textSurface.get_rect(center=textPos)
            self.image.blit(self.textSurface, textPos)
            self.altImg.blit(self.textSurface, textPos)

    def touching_Mouse(self, pos):
        return self.rect.collidepoint(pos)

    def change(self):
        if self.altImg == 0:
            return
        self.image, self.altImg = self.altImg, self.image


def init_window_birb():
    global b1, birb_pic
    birb_pic = pygame.image.load(birb_pic).convert_alpha()
    birb_pic = pygame.transform.scale(birb_pic, (40, 15))
    s = Sprite(sight)
    s.ogImg = pygame.transform.scale(s.image, (birb.sight_radius, birb.sight_radius))
    sight_group.add(s)
    for i in range(num_of_birbs):
        b = Sprite(birb_pic, i)
        if i == 0:
            b1 = b
        sprite_group.add(b)


def moveAllBirbs():
    for i in sprite_group:
        i.moveBy(birb.birb_list)
        i.rotate(birb.birb_list)
        if viswals:
            for j in sight_group:
                j.moveBy(birb.birb_list)
                j.rotate(birb.birb_list)
    # circle.rect.center = birb.circlePos  # ts------------

# use pygme gui
# multiple viswal sprite to make it accurate
def init_gui():  # make pull down tab for gui and add sliders for speed and sight
    global buttons
    separation_button = Gui(pressed_button, unpressed_button, (155, 33), (WINDOW_WIDTH - 130, 70), "separation")
    alignment_button = Gui(pressed_button, unpressed_button, (155, 33), (WINDOW_WIDTH - 130, 120), "alignment")
    cohesion_button = Gui(pressed_button, unpressed_button, (155, 33), (WINDOW_WIDTH - 130, 170), "cohesion")
    visuals_button = Gui(pressed_button, unpressed_button, (155, 33), (WINDOW_WIDTH - 130, 220), "visuals")
    pause_button = Gui(pause, play, (24, 26), (WINDOW_WIDTH - 180, 280))
    step_button = Gui(step, False, (35, 29), (WINDOW_WIDTH - 110, 281))
    buttons = [separation_button, alignment_button, cohesion_button, visuals_button, pause_button, step_button]
    for i in buttons:
        gui_group.add(i)


def gui():
    global play, step, viswals
    for count, i in enumerate(buttons):
        if i.touching_Mouse(pygame.mouse.get_pos()):
            i.change()
            if count < 3:
                birb.filters[count] = not birb.filters[count]
            elif count == 3:
                viswals = not viswals
            elif count == 4:
                play = not play
            else:
                step = True


birb.init()
# birb.ts()
# birb.test()
num_of_birbs = birb.num_of_birbs
pygame.init()
SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), SURFACE)

sprite_group = pygame.sprite.Group()  # All sprites for updating and drawing
sight_group = pygame.sprite.Group()
gui_group = pygame.sprite.Group()
init_gui()
init_window_birb()

# -------ts
# circle = Sprite(circle)
# sprite_group.add(circle)
# circle.ogImg = pygame.transform.scale(circle.ogImg, (14, 14))
# -------

clock = pygame.time.Clock()
done = False
temp = 0
step = True
play = not False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            gui()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                step = True
            elif event.key == pygame.K_p:
                play = not play

    Mouse_x, Mouse_y = pygame.mouse.get_pos()  # remove all ts stuff like the mouse
    if step or play:
        birb.main(Mouse_x, Mouse_y)
        moveAllBirbs()

    # Repaint the screen
    if viswals:
        b1.ogImg = pygame.image.load(birb_touch).convert_alpha()  # fix
        b1.ogImg = pygame.transform.scale(b1.ogImg, (40, 15))
        sight_group.update()
    else:
        b1.ogImg = birb_pic
    sprite_group.update()  # re-position the game sprites
    gui_group.update()
    window.fill((100, 100, 100))

    if viswals:  # somehow order sight to back to not cover the birbs--------------------------------------------
        sight_group.draw(window)
    sprite_group.draw(window)  # draw the game sprites
    gui_group.draw(window)

    step = False

    pygame.display.flip()
    clock.tick_busy_loop(60)
    # time.sleep(0.1)

pygame.quit()

import pygame
from birbs import birb_code

white = (100, 100, 100)
display_width, display_height = birb_code.display_width, birb_code.display_height
GD = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()  # FPS stuff
crashed = False
birb_pic = pygame.image.load(r'/home/agmui/Desktop/pyImages/birb.png')
#green_birb_pic = pygame.image.load(r'C:\Users\antho\Desktop\pyImages\birb_touch.png')
sight_pic = pygame.image.load(r'/home/agmui/Desktop/pyImages/sight.png')
birbs = birb_code.birbs
pause = True


while not crashed:
    pause = birb_code.events(pause)
    if not pause:
        GD.fill(white)

        """Mouse_x, Mouse_y = pygame.mouse.get_pos()
        birbs[1] = Mouse_x, Mouse_y, 270"""

        for i in range(len(birbs)):
            #if i != 1:
            birbs[i][0], birbs[i][1] = birb_code.wall(birbs[i][0], birbs[i][1])
            data = []
            for j in range(len(birbs)):
                if i != j:
                    hit = birb_code.collision(birbs[i], birbs[j][0], birbs[j][1], j)
                    data.append(hit)
            # pathfinding code
            birbs[i] = list(birb_code.path_finding(birbs[i][0], birbs[i][1], birbs[i][2], data, i))

        birb_obstical = birb_code.Draw(birb_pic)
        for i in range(len(birbs)):
            birb_obstical.draw(birbs[i])

        #sight = birb_code.Draw(sight_pic)
        #sight.draw(birbs[1])

    pygame.display.update()
    clock.tick(60)
    #time.sleep(0.1)

pygame.quit()
quit()

import pygame
import time

pygame.init()
table = pygame.image.load(r'C:\Users\antho\Desktop\pyImages\table.png')
gameDisplay = pygame.display.set_mode((527, 527))
clock = pygame.time.Clock()
crashed = False
font = pygame.font.SysFont("Comic Sands MS", 35)
solved = False
br = []
for i in range(9):
    br.append((i / 9) * 507 + (507 / 18) + 5)
bf = list(br)

# input problem
x = [
    2, 4, 5, 0, 0, 1, 0, 0, 0,
    0, 0, 0, 0, 6, 0, 3, 0, 8,
    0, 0, 0, 0, 9, 2, 0, 0, 0,
    0, 0, 0, 0, 2, 8, 0, 3, 0,
    4, 0, 8, 3, 0, 0, 0, 1, 0,
    7, 9, 0, 4, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 9, 0, 0, 0,
    3, 0, 0, 0, 7, 0, 6, 0, 2,
    0, 6, 0, 0, 0, 0, 5, 4, 0]

n = 0
r = 0
f = 0
b = 1
rows = [x[0:9], x[9:18], x[18:27], x[27:36], x[36:45], x[45:54], x[54:63], x[63:72], x[72:81]]
files = [1, 2, 3, 4, 5, 6, 7, 8, 9]
blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9]
store = list(x)
pos = [
    (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 2), (0, 0, 2), (0, 0, 2), (0, 0, 3), (0, 0, 3), (0, 0, 3),
    (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 2), (0, 0, 2), (0, 0, 2), (0, 0, 3), (0, 0, 3), (0, 0, 3),
    (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 2), (0, 0, 2), (0, 0, 2), (0, 0, 3), (0, 0, 3), (0, 0, 3),
    (0, 0, 4), (0, 0, 4), (0, 0, 4), (0, 0, 5), (0, 0, 5), (0, 0, 5), (0, 0, 6), (0, 0, 6), (0, 0, 6),
    (0, 0, 4), (0, 0, 4), (0, 0, 4), (0, 0, 5), (0, 0, 5), (0, 0, 5), (0, 0, 6), (0, 0, 6), (0, 0, 6),
    (0, 0, 4), (0, 0, 4), (0, 0, 4), (0, 0, 5), (0, 0, 5), (0, 0, 5), (0, 0, 6), (0, 0, 6), (0, 0, 6),
    (0, 0, 7), (0, 0, 7), (0, 0, 7), (0, 0, 8), (0, 0, 8), (0, 0, 8), (0, 0, 9), (0, 0, 9), (0, 0, 9),
    (0, 0, 7), (0, 0, 7), (0, 0, 7), (0, 0, 8), (0, 0, 8), (0, 0, 8), (0, 0, 9), (0, 0, 9), (0, 0, 9),
    (0, 0, 7), (0, 0, 7), (0, 0, 7), (0, 0, 8), (0, 0, 8), (0, 0, 8), (0, 0, 9), (0, 0, 9), (0, 0, 9), ]
temp_store = []


def back(n):
    n -= 1
    while type(store[n]) == int:
        n -= 1
    if len(store[n]) == 1:
        x[n] = 0
        store[n] = []


        #printing--------------------------
        print_board()
        """
        n2 = 0
        for i in range(81):
            if x[n2] != 0:
                time.sleep(0.00005)
                text(x[n2], br[(pos[n2][1]) - 1], bf[(pos[n2][0]) - 1])
            n2 += 1
            """
        #printing--------------------------
        back(n)
    else:
        if x[n] == store[n][-1]:  # if on last posible
            x[n] = 0
            store[n] = [0]
            # printing--------------------------
            print_board()
            """
            n2 = 0
            for i in range(81):
                if x[n2] != 0:
                    time.sleep(0.00005)
                    text(x[n2], br[(pos[n2][1]) - 1], bf[(pos[n2][0]) - 1])
                n2 += 1
                """
            # printing--------------------------
            back(n)
        else:
            place = store[n].index(x[n])
            place += 1
            x[n] = store[n][place]
            place = 0
            # printing--------------------------
            print_board()
            """
            n2 = 0
            for i in range(81):
                if x[n2] != 0:
                    time.sleep(0.00005)
                    text(x[n2], br[(pos[n2][1]) - 1], bf[(pos[n2][0]) - 1])
                n2 += 1
            """
            # printing--------------------------


def update():
    # update rows
    rows = [x[0:9], x[9:18], x[18:27], x[27:36], x[36:45], x[45:54], x[54:63], x[63:72], x[72:81]]

    n = 0
    # update files
    for i in range(9):
        z = 0
        for i in range(9):
            files[n] = [x[0 + n], x[9 + n], x[18 + n], x[27 + n], x[36 + n], x[45 + n], x[54 + n], x[63 + n], x[72 + n]]
            z += 1
        n += 1
    n = 0
    # update blocks <---improve
    blocks = [x[0:2] + x[9:11] + x[18:20], x[3:5] + x[12:14] + x[21:23], x[6:8] + x[15:17] + x[24:26],
              x[27:29] + x[36:38] + x[45:47], x[30:32] + x[39:41] + x[48:50], x[33:35] + x[42:44] + x[51:53],
              x[63:65] + x[72:74] + x[81:83], x[66:68] + x[75:77] + x[84:86], x[69:71] + x[78:80] + x[87:89]]


update()  # <--------rows and blocks dont get updated in update function
rows = [x[0:9], x[9:18], x[18:27], x[27:36], x[36:45], x[45:54], x[54:63], x[63:72], x[72:81]]
blocks = [x[0:3] + x[9:12] + x[18:21], x[3:6] + x[12:15] + x[21:24], x[6:9] + x[15:18] + x[24:27],
          x[27:30] + x[36:39] + x[45:48], x[30:33] + x[39:42] + x[48:51], x[33:36] + x[42:45] + x[51:54],
          x[63:66] + x[72:75] + x[81:84], x[66:69] + x[75:78] + x[84:87], x[69:72] + x[78:81] + x[87:90]]


def text(n, x, y):
    text = font.render(str(n), True, (0, 0, 0))
    gameDisplay.blit(text, (x, y))
def Rect(n):
    Rect = pygame.Rect(0, 0, 40, 40)
    Rect.center = (br[(pos[n][1]) - 1] + 7, bf[(pos[n][0]) - 1] + 7)
    pygame.draw.rect(gameDisplay, (255, 255, 255), Rect)
def print_board():
    n2 = 0
    for i in range(81):
        if x[n2] != 0:
            text(x[n2], br[(pos[n2][1]) - 1], bf[(pos[n2][0]) - 1])
        n2 += 1
    pygame.display.update()

# pos(position)for rows files and blocks
z = 0
for i in range(81):
    if n == 0:
        r = 0

    # row
    if n % 9 == 0:
        r += 1
    else:
        r = r

    # file
    f = (n + 1) % 9
    if f == 0:
        f = 9

    # block help
    b = pos[n]
    b = b[2]

    pos[n] = (r, f, b)
    n += 1

n=0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    gameDisplay.fill((255, 255, 255))
    gameDisplay.blit(table, (10, 10))

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if x[n] == 0:
        temp_store = []
        z = 1
        a, b, c = pos[n]

        for i in range(9):
            if z in rows[a - 1] + files[b - 1] + blocks[c - 1]:  # <----check if blocks[c-1] is correct

                # printing--------------------------
                #time.sleep(1)#ts
                Rect(n)
                text(z, br[(pos[n][1]) - 1], bf[(pos[n][0]) - 1])# <-----posibilatys stacking when priting
                
                print_board()
                """
                n2 = 0
                for i in range(81):
                    if x[n2] != 0:
                        text(x[n2], br[(pos[n2][1]) - 1], bf[(pos[n2][0]) - 1])
                    n2 += 1
                pygame.display.update()
                """

                # printing--------------------------
                z += 1
            else:
                temp_store.append(z)
                z += 1
        store[n] = temp_store

        if len(temp_store) == 0:
            back(n)
            n = 0
        else:
            x[n] = temp_store[0]
        update()
        rows = [x[0:9], x[9:18], x[18:27], x[27:36], x[36:45], x[45:54], x[54:63], x[63:72], x[72:81]]
        blocks = [x[0:3] + x[9:12] + x[18:21], x[3:6] + x[12:15] + x[21:24], x[6:9] + x[15:18] + x[24:27],
                  x[27:30] + x[36:39] + x[45:48], x[30:33] + x[39:42] + x[48:51], x[33:36] + x[42:45] + x[51:54],
                  x[63:66] + x[72:75] + x[81:84], x[66:69] + x[75:78] + x[84:87], x[69:72] + x[78:81] + x[87:90]]
    n += 1


    if n == 81:
        solved = True
        print(solved)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #printing text
    n2=0
    for i in range(81):
        if x[n2]!=0:
            time.sleep(0.00005)
            text(x[n2],br[(pos[n2][1])-1],bf[(pos[n2][0])-1])
        n2+=1

    pygame.display.update()
    clock.tick(60)


    if solved:#<----------------change/solve to not do this
        time.sleep(100)
        break

pygame.quit()
quit()

print("ans")
print(x[0:9])
print(x[9:18])
print(x[18:27])
print(x[27:36])
print(x[36:45])
print(x[45:54])
print(x[54:63])
print(x[63:72])
print(x[72:81])


#import numpy as np

grid = [[0] * 100 for i in range(100)]
x, y = 5, 5
direction = "N"
none = 0
red = 1
white = 2

def turnL():
    global x, y, direction

    if direction == "N":
        y -= 1
        direction = "W"
        # print("n")
    elif direction == "S":
        y += 1
        direction = "E"
        # print("s")
    elif direction == "E":
        x -= 1
        direction = "N"
        # print("e")
    elif direction == "W":
        x += 1
        direction = "S"
        # print("w")


def turnR():
    global x, y, direction

    if direction == "N":
        y += 1
        direction = "E"
        # print("n")
    elif direction == "S":
        y -= 1
        direction = "W"
        # print("s")
    elif direction == "E":
        x += 1
        direction = "S"
        # print("e")
    elif direction == "W":
        x -= 1
        direction = "N"
        # print("w")


def ant():
    global x, y
    if grid[x][y] == none:
        grid[x][y] = red
        turnL()

    elif grid[x][y] == white:
        grid[x][y] = red
        turnL()

    else:
        grid[x][y] = white
        turnR()

def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

"""
for i in range(3):
    ant()
    l = []
    for i in range(100):
        l.append(indices(grid[i],1))
    print(l)
hi=[1]
if  any(item in l for item in hi for l in (grid[1])):
    print(True)
"""

for i in range(12):
    ant()
    print()
    for i in range(100): 
        print(grid[i])


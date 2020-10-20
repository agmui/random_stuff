import copy

size = 100
grid = [[0] * size for i in range(size)]
grid_2 = [[0] * size for i in range(size)]

none = 0
white = 1



def step():
    global grid, grid_2
    for i in range(size):
        grid_2[i] = grid[i] + []
    for i2 in range(size):
        for i, val in enumerate(grid[i2]):
            points = 0

            try:
                if grid[i2][i - 1] == 1:
                    points += 1
            except IndexError:
                pass
            try:
                if grid[i2][i + 1] == 1:
                    points += 1
            except IndexError:
                pass
            try:
                if grid[i2 - 1][i] == 1:
                    points += 1
            except IndexError:
                pass
            try:
                if grid[i2 + 1][i] == 1:
                    points += 1
            except IndexError:
                pass
            try:
                if grid[i2 - 1][i - 1] == 1:
                    points += 1
            except IndexError:
                pass
            try:
                if grid[i2 + 1][i - 1] == 1:
                    points += 1
            except IndexError:
                pass
            try:
                if grid[i2 - 1][i + 1] == 1:
                    points += 1
            except IndexError:
                pass
            try:
                if grid[i2 + 1][i + 1] == 1:
                    points += 1
            except IndexError:
                pass

            #print(points)
            if points == 3:  # spawn
                grid_2[i2][i] = 1

            elif points in range(2,3):  # alive code
                if grid[i2][i] == 1:
                    grid_2[i2][i] = 1
                    #print("alive")

            elif points in range(2):  # death
                grid_2[i2][i] = 0
                #print("dead")

            elif points >= 4:  # death
                grid_2[i2][i] = 0

            #print(f'({i}, {i2})')
    for i in range(size):
        grid[i] = grid_2[i] + []

"""
for i in range(1):
    print()
    step()
    for i in range(size):
        print(grid[i])"""

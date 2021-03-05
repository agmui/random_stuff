# input problem
grid = [
    [2, 4, 5, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 3, 0, 8],
    [0, 0, 0, 0, 9, 2, 0, 0, 0],
    [0, 0, 0, 0, 2, 8, 0, 3, 0],
    [4, 0, 8, 3, 0, 0, 0, 1, 0],
    [7, 9, 0, 4, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 9, 0, 0, 0],
    [3, 0, 0, 0, 7, 0, 6, 0, 2],
    [0, 6, 0, 0, 0, 0, 5, 4, 0]]


def check(x, y, n):
    global grid
    for i in range(len(grid)):
        if grid[y][i] == n:
            return False
    for i in range(len(grid)):
        if grid[i][x] == n:
            return False
    x = int(x / 3) * 3
    y = int(y / 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y + i][x + j] == n:
                return False
    return True


def main():
    global grid
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if check(j, i, n):
                        grid[i][j] = n
                        main()
                        grid[i][j] = 0
                return

    for i in range(len(grid)):
        print(grid[i])


if __name__ == "__main__":
    main()
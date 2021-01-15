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


def check(x, y):
    n = grid[y][x]
    if n == 0:
        return 0
    ans = False
    grid[y][x] = 0
    for i in grid[y]:
        if i == n:
            ans = True
    for i in range(len(grid)):
        if grid[i][x] == n:
            ans = True
    grid[y][x] = n
    return ans


def test():
    for i in range(8):
        for j in range(8):
            if check(i, j):
                print(i, j)
                break


def main():
    global grid
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                while check(j, i) == 0 or check(j, i):
                    grid[i][j] += 1
                    if grid[i][j] == 9:
                        grid[i][j] = 0
                        return 0
                """print()
                for i in range(len(grid)):
                    print(grid[i])"""
                main()
                grid[i][j] += 1


if __name__ == "__main__":
    main()
    for i in range(len(grid)):
        print(grid[i])

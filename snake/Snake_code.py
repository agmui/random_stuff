size = 50
grid = [[0] * size for i in range(size)]
direction = "N"
score = 3

grid[int(size / 2)][int(size / 2)] = 1
grid[int(size / 2 - 1)][int(size / 2)] = 2
grid[int(size / 2 - 2)][int(size / 2)] = 3


class snake:
    def __init__(self, direction, score, grid):
        self.direction = direction
        self.score = score
        self.grid = grid
        self.old_x, self.old_y = 0, 0
        self.death = False
        self.head_x, self.head_y = 0, 0
        self.body_x, self.body_y = [], []

    def head(self):
        d = dict((j, (x, y)) for x, i in enumerate(self.grid) for y, j in enumerate(i))
        y, x = d[self.score]

        if self.direction == "N":
            if y == 0:
                self.death = True
                return True
            else:
                self.grid[y - 1][x] = self.score
        elif self.direction == "S":
            if y == size - 1:
                self.death = True
                return True
            else:
                self.grid[y + 1][x] = self.score

        elif self.direction == "E":
            if x == size - 1:
                self.death = True
                return True
            else:
                self.grid[y][x + 1] = self.score
        else:
            if x == 0:
                self.death = True
                return True
            else:
                self.grid[y][x - 1] = self.score
        self.old_x, self.old_y = x, y
        self.head_x, self.head_y = x, y

    def body(self):
        d = dict((j, (x, y)) for x, i in enumerate(self.grid) for y, j in enumerate(i))
        n = 1
        if self.death:  # fix
            return True
        for i in range(self.score - 1):
            result = any(n in sublist for sublist in grid)
            if not result:
                return True
            n += 1

        for i in range(self.score - 1):
            y, x = d[self.score - (i + 1)]
            grid[self.old_y][self.old_x] = self.score - (i + 1)
            self.old_x, self.old_y = x, y

            if len(self.body_x) < self.score - 1:
                self.body_x.append(x)
            else:
                self.body_x[i] = x
            if len(self.body_y) < self.score - 1:
                self.body_y.append(y)
            else:
                self.body_y[i] = y
        else:
            grid[y][x] = 0

        return False


if __name__ == '__main__':
    for i in range(3):
        for i in range(size):
            print(grid[i])
        print()
        test = snake(direction, score, grid)
        test.head()
        test.body()

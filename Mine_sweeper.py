import random

# 0 is unknown, -1 is non space, -2 in mine
board = [[0] * 8 for i in range(8)]
# number of mines
n_mines = 10
# spawning mines

while sum(sum(board, [])) > -2 * n_mines + 1:
    board[random.randint(0, len(board) - 1)][random.randint(0, len(board)) - 1] = -2


# click thing
def check_surrounding_tiles(x, y):
    help = board[x - 1][y - 1] + board[x][y - 1] + board[x + 1][y - 1] + board[x - 1][y] + board[x + 1][y] + \
           board[x - 1][y + 1] + board[x][y + 1] + board[x + 1][y + 1]
    return help//-2


class Sweeper:
    def __init__(self):
        self.score = 0

    def show_board(self):
        for i in range(len(board)):
            print(board[i])

    def click(self, x, y):
        if board[x][y] == 0:
            # look at all surrounding tiles
            num = check_surrounding_tiles(x, y)
            print(num)
            if num == 0:
                board[x][y] = -1
                # expand code
            else:
                board[x][y] = num
                # expand code if allowed

            # board[x][y] = (-1 if num == 0 else num)

        else:
            # die
            print("game over")


Mine = Sweeper()
Mine.show_board()
Mine.click(4, 4)
Mine.show_board()

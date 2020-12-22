def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n - 1) + n


# print(sum(4,2))


def grid(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return grid(n - 1, m) + grid(n, m - 1)


# print(grid(4,2))

def count(n, m):
    if n == 0:
        return 1
    if m == 0 or n < 0:
        return 0
    else:
        return count(n, m - 1) + count(n - m, m)


print(count(6, 4))

"""
count(1,1) = 1
o | o
o
count(2,2)
o o | o o
o o
o + o
count(3,3)
o o o | o o o
o o o
o o + o
o + o + o
count(4,4) = count(4,3) + 1 = 5


count(1,3) = 1
o | o o o
o

count(2,3) = count(1,3) + 1 = 2
o o | o o o
o o
o + o

count(3,3) = count(1,3) + 1 = 3
o o o
o o + o
o + o + o

count(3,2) = 2
o o o o o | o o
o o + o
o + o + o

count(4,2) =count(3,2)+1= 3
o o o o o | o o
o o + o o
o o + o + o
o + o + o + o

count(5,2) =count(5,2)+0= 3
o o o o o o| o o
o o + o o + o
o o + o + o + o
o + o + o + o + o 

count(6,2) = count(5,2) + 1 = 4
o o o o o o| o o
o o + o o + o o
o o + o o + o + o
o o + o + o + o + o
o + o + o + o + o + o


count(6,1) = 1
o o o o o o| o
o + o + o + o + o + o

count(6,2) = count(6,1) + 3 = 4
o o o o o o| o o
o o + o o + o o
o o + o o + o + o
o o + o + o + o + o
o + o + o + o + o + o

count(6,3) = count(6,2) + 3 = 7
o o o o o o| o o o
o o o + o o o
o o o + o o + o
o o o + o + o + o
o o + o o + o o + o
o o + o o + o + o + o
o o + o + o + o + o + o
o + o + o + o + o + o + o

count(6,4) = count(6,3) + 2 = 9
o o o o o o| o o o o
o o o o + o o
o o o o + o + o
o o o + o o o + o
o o o + o o + o + o
o o o + o + o + o + o
o o + o o + o o + o + o
o o + o o + o + o + o + o
o o + o + o + o + o + o + o
o + o + o + o + o + o + o + o

count(6,5) = count(6,4) + 1 = 10
o o o o o o| o o o o o
o o o o o + o
o o o o + o o
o o o o + o + o
o o o + o o o
o o o + o o + o
o o o + o + o + o
o o + o o + o o
o o + o o + o + o
o o + o + o + o + o
o + o + o + o + o + o

count(6,6) = count(6,5) + 1 = 11

count(5,5) = 7

count(2,1) = 1
o o| o
o + o

count(2,2) = count(2,1) + 1
o o | o o
o o
o + o

count(2,3) = count(2,2) + 1
o o | o o
o o
o o + o
o + o + o


count(3,1) = 1
o o o| o
o + o + o

count(3,2) = count(3,1) + 1
o o o | o o
o o + o
o + o + o

count(3,3) = count(3,2) + 1
o o o|o o o
o o o
o o + o
o + o + o

count(4,1) = 1
o + o + o + o

count(4,2) = count(4,1) + 2 = 3
o o + o o
o o + o + o
o + o + o + o

count(4,3) = count(4,2) + 1 = 4
o o o + o
o o + o o
o o + o + o
o + o + o + o

count(4,4) = count(4,3) + 1 = 5

"""

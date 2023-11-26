finalSeq = "none"
ringNum = input("rings: ")
order = []


def ringOrder(start, end, helper, n):
    global order
    if n == 1:
        order.append([start, end])
        return order
    else:
        ringOrder(start, helper, end, int(n) - 1)
        order.append([start, end])
        ringOrder(helper, end, start, int(n) - 1)


def MoveTower(rings):  # < ---------- finds sequence
    global finalSeq
    if int(rings) < 2:
        print(finalSeq)
    elif int(rings) == 2:
        finalSeq = "1 2 1"
        return finalSeq
    elif int(rings) > 2:
        finalSeq = MoveTower(int(rings) - 1) + " " + str(rings) + " " + MoveTower(int(rings) - 1)
        return finalSeq


def moveRing(rings):
    global ringNum
    ringOrder("A", "B", "C", ringNum)
    ringSeq = MoveTower(rings)
    ringArr = ringSeq.split()
    for i in range(steps):
        print("Move ring " + ringArr[i] + " from tower " + order[i][0] + " to tower " + order[i][1])



steps = (2 ** int(ringNum)) - 1
MoveTower(ringNum)
print("Sequence: " + finalSeq)
print("Moves: " + str(steps))
moveRing(ringNum)
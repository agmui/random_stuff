l = [(1, False)]


def collatz_Conjecture(n):
    if n / 2 == int(n / 2):
        return n / 2
    else:
        return 3 * n + 1


def function(n):
    if (n - 1) / 3 == int((n - 1) / 3) and (n - 1) / 3 != 0 and (n - 1) / 3 != 1:
        send = int((n - 1) / 3)
    else:
        send = None
    return n * 2, send


def plzhelp(root, thing, i):
    input, input2 = thing
    l[i] = [root, input, input2, True, -1, -1]
    # l.append((root, input, input2, True))
    return input, input2


# print(function(1))
out1_new, out2_new = plzhelp(1, function(1), 0)
save = 0
while len(l) < 101:
    out1, out2 = out1_new, out2_new
    if out1 is not None and out2 is not None:
        l.append((out1, False))
        l.append((out2, False))
    elif out1 is not None and out2 is None:
        l.append((out1, False))
    else:
        l.append((out2, False))
    for i in range(save, len(l)):
        if not l[i][1]:
            out1_new, out2_new = plzhelp(l[i][0], function(l[i][0]), i)
            save = i
            break

if __name__ == "__main__":
    print(l)

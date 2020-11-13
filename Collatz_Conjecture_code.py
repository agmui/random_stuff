
input = [1, 2, 3, 4]
l = []

def collatz_Conjecture(n):
    if n / 2 == int(n / 2):
        return n / 2
    else:
        return 3 * n + 1

def function(n):
    send = -1
    if (n - 1) / 3 == int((n - 1) / 3) or (n - 1) / 3 != 0 or (n - 1) / 3 != 1:
        send = 3 * (n + 1)
    return n * 2, send

def plzhelp(past, thing):
    input, input2 = thing
    l.append((past, input, input2))
    if input is not None and input2 is not None:
        plzhelp(input, function(input))
        plzhelp(input2, function(input2))
    elif input is not None and input2 is None:
        plzhelp(input, function(input))
    else:
        plzhelp(input2, function(input))


print(function(input[1]))
for i in range(len(input)):
    plzhelp(1, function(input[i]))

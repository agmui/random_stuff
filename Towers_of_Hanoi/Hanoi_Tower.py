"""n = int(input("input # of rings: "))
main = []
past = [1]
steps = [1]
steps_2 = []
rings = [[], [], []]
data = []


def move(list, old, new):
    list[new - 1].insert(0, list[old - 1][0])
    list[old - 1].pop(0)


for i in range(n - 1):
    main = past + []
    main.append(i + 2)
    main += past
    past = main

print(f'ring: {main}')
data.append(("main:", main))

for i in range(round((len(main) - 1) / 3)):
    steps.append(2)
    steps.append(1)
    steps.append(1)
    if len(main) < len(steps):
        steps.pop()
    steps_2.append(2)
    steps_2.append(1)
    steps_2.append(1)
    if len(main) < len(steps_2):
        steps_2.pop()

print(f'steps: {steps}')
data.append(("steps:", steps))

# ---------------------------------------------------------------
print("---------")
print()

for i in range(n):
    rings[0].append(i + 1)

print(rings)

if len(rings[0]) / 2 > int(len(rings[0]) / 2):
    print("swap")
    temp = []  # <-----------------swap
    temp = steps + []
    steps = []
    steps = steps_2
    steps_2 = []
    steps_2 = temp + []

for i in range(len(steps)):
    if main[i] in rings[0]:  # <----------make better
        tower = 1
        move(rings, tower, tower + steps[i])
    elif main[i] in rings[1]:
        tower = 2

        temp = []  # <-----------------swap
        temp = rings[1] + []
        rings[1] = []
        rings[1] = rings[2]
        rings[2] = []
        rings[2] = temp + []
        move(rings, 3, 3 - steps_2[i])
        temp = []  # <-----------------swap
        temp = rings[1] + []
        rings[1] = []
        rings[1] = rings[2]
        rings[2] = []
        rings[2] = temp + []

    else:
        tower = 3
        move(rings, tower, tower - steps[i])

    if len(main) == i + 2:
        if len(rings[0]) / 2 > int(len(rings[0]) / 2):
            move(rings, 1, 3)
        print(f'{rings} step: {i + 1}')
        data = data + rings
    else:
        print(f'{rings} step: {i + 1}')
        data = data + rings"""


def move(r, LR):
    index = -1
    for i in rings:
        index += 1
        if r in i:
            if LR == 'R':
                if index != 2:
                    rings[index + 1].insert(0, i[0])
                else:
                    rings[0].insert(0, i[0])
                rings[index].pop(0)
            elif LR == 'L':
                if index != 0:
                    rings[index - 1].insert(0, i[0])
                else:
                    rings[2].insert(0, i[0])
                rings[index].pop(0)
            break


# move(1, 'R')
def main(x):
    if x == 0:
        pass
    else:
        main(x - 1)
        move(x, 'R' if x % 2 == 0 else 'L')
        main(x - 1)


x = 5
rings = [[1, 2, 3, 4, 5], [], []]
for i in range(2 if x % 2 == 0 else 1):
    main(x)
print(rings)

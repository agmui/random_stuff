import random

G1 = []
for i in range(26):
    G1.append(i + 1)
G1.append(0)
mix = [G1.copy() + [], G1.copy() + [], G1.copy() + []]
G2, G3, seed = G1.copy(), G1.copy(), G1.copy()

alphabet = ["_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u",
            "v", "w", "x", "y", "z"]
save = []
x = []
text = []
output = []
scramble = []


def rotate(gear, r):
    for i in range(r):
        gear.append(gear[0])
        gear.pop(0)


def translate(in_, x, out_, ):
    return in_[mix[x][out_]]


def magic(numList):  # [1,2,3]
    s = map(str, numList)  # ['1','2','3']
    s = ''.join(s)  # '123'
    s = int(s)  # 123
    return s


# generate randomness code-----------------------------------------------------------------

random.shuffle(seed)
# print(f'seed: {magic(seed)}')

for i in range(26):
    G1.insert(seed[i], G1[-1])
    G1.pop()
G2, G3 = G1.copy(), G1.copy()

# input_ code-----------------------------------------------------------------

print()
input_ = " " + input("input text: ")  # <--------- must have front space bc it is buggy for some reason?
# print(input_)
input_ = input_.replace(" ", "_")

# convert code-----------------------------------------------------------------

for i in range(len(alphabet)):
    old = 0
    while old <= len(input_) - 1:
        if type(input_.find(alphabet[i], old)) == int:
            x.append(input_.find(alphabet[i], old))
            old = x[-1] + 1
        if input_.find(alphabet[i], old) < 1:
            break

    save.append(x + [])

    x.clear()

for i in range(len(input_)):
    text.append(0)

letter = -1
for i in range(len(save)):
    letter += 1
    something = save[i]
    if something[0] > 0:
        for i in range(len(something)):
            text[something[i]] = letter
text.pop(0)
# ---------------------------------------------------------------------------------------

rotate(mix[0], seed[0] + 26)  # <---seed goes in here and plz keep +26
rotate(mix[1], seed[1] + 26)
rotate(mix[2], seed[2] + 26)
# ^ eveything above is just setup
# important part of code
count1, count2 = 0, 0
for i in range(len(text)):
    output.append(translate(G3, 2, translate(G2, 1, translate(G1, 0, text[i]))))
    count1 += 1
    rotate(mix[0], 1)
    if count1 == 26:
        rotate(mix[1], 1)
        count2 += 1
        count1 = 0
    if count2 == 26:
        rotate(mix[2], 1)
        count2 = 0

index = 0
for i in output:
    output[index]=alphabet[i]
    index += 1


final_output = ""
for i in range(len(output)):
    final_output = output[i]+ final_output
print()
print("seed :")
print(magic(seed))
print("--------------------------------------------")
print("output:")
print(final_output)

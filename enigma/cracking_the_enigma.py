G1 = []
for i in range(26):
    G1.append(i + 1)
G1.append(0)
G2, G3 = G1.copy(), G1.copy()


seed = input("input seed: ")
input_ = input("input enigma text: ")

print(input_)
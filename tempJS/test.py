import json

with open('sort.json') as f:
    cards = json.load(f)

if input('jump?[y][N]: ') == 'y':
    num = int(input('to: '))
    with open('sort2.json') as f:
        data = json.load(f)
else:
    num = 0
    data = [
        [
            "Upgrade",
            ["Move"],
            ["Ban"],
            ["Other"]
        ],
        [
            "Downgrade"
        ],
        [
            "Magic"
        ]
    ]

print('\n==Options: 1 Move, 2 Ban, 3 Other==\n')

lastAction = 0
while num != len(cards[0]):
    i = cards[0][num]
    try:
        print(i["text"])
        ans = input("\ninput[1] [2] [3] [u] [save]: ")
        print("chose:", ans)
        print("========================")
        num += 1
        if ans == "1":
            data[0][1].append(i)
            lastAction = 1
        elif ans == "2":
            data[0][2].append(i)
            lastAction = 2
        elif ans == "3":
            data[0][3].append(i)
            lastAction = 3
        elif ans == "u":
            if lastAction != 0:
                num -= 2
                data[0][lastAction].pop()
            else:
                num-=1
                print('\n==no previous action==\n')
        elif ans == "save":
            print("where you stoped:", num-1)
            break
        else:
            num -= 1
            print("\n==invalid input==\n")
        with open('sort2.json', 'w') as json_file:
            json.dump([], json_file)
        with open('sort2.json', 'w') as json_file:
            json.dump(data, json_file)
    except:
        print('==unkown==')
        print("========================")
        num += 1

with open('sort2.json', 'w') as json_file:
    json.dump(data, json_file)

import json

with open('./sort.json') as f:
  cards = json.load(f)

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
print(cards[0])
for i in cards[0]:
  try:
    print(i["text"])
  except:
    print('unkown')
  ans = input("input[a] [b] [c]: ")
  print("chose:", ans)
  print("========================")
  if ans == "a":
    data[0][1].append(ans)
  elif ans == "b":
    data[0][2].append(ans)
  elif ans == "c":
    data[0][3].append(ans)
  else:
    print("invalid input")

with open('sort2.json', 'w') as json_file:
  json.dump(data, json_file)
l = [[1,[2,2]], [1, [2,2]]]

total = list(i[1] for i in l)
total2 = sum(i[1] for i in (i[1] for i in l))
print(total2)
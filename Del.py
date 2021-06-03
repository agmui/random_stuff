"""cowList = [['bes', 1]]
# print("N: ", end='')
# num = int(input())
num = 2


def main():
    global cow1, pn, z, cow2
    past = 1
    for i in range(num):
        #print("format: cow1, previos/next, animal, cow2")
        #cow1=input()
        #pn=input()#precios/next
        #z=input()#animal or zodiac
        #cow2=input()
        if i == 0:
            cow1, pn, z, cow2 = "a", "next", 2, "bes"
        if i == 1:
            cow1, pn, z, cow2 = "b", "next", 4, "bes"
        if i == 2:
            cow1, pn, z, cow2 = "a", "next", 1, "bes"
        if i == 3:
            cow1, pn, z, cow2 = "a", "next", 1, "bes"
        # animal convert
        # 1 ox, 2 tigar ... 12 rat
        # ====================================================================

        if cow2 not in cowList:
            print(cow2, 'not in list')
            return
        if cow1 in cowList:
            print(cow1, 'already mentioned')
            return
        if pn == "next":
            pn = 1
        else:
            pn = -1
        cowList.append([cow1, pn*z+past])
        past = pn*z+past


main()"""

if []:
    print(1)
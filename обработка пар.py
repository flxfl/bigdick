n = int(input())
line = []
trash = 0
o0 = 1000000
po0 = 1000000
o1 = 1000000
po1 = 1000000
o2 = 1000000
po2 = 1000000
min_summ = 1000000
mina, minb = [0, 0]
for i in range(5):
    line.append(int(input()))
for i in range(5, n):
    x = int(input())
    trash = line[i % 5]
    if x % 2 == 1:
        if (x % 3 == 0) and (x < o0):
            po0 = o0
            o0 = x
        elif (x % 3 == 0) and (x < po0):
            po0 = x
        elif (x % 3 == 1) and (x < o1):
            po1 = o1
            o1 = x
        elif (x % 3 == 1) and (x < po1):
            po1 = x
        elif (x % 3 == 2) and (x < o2):
            po2 = o2
            o2 = x
        elif (x % 3 == 2) and (x < po2):
            po2 = x
    if trash % 2 == 1:
        if (trash % 3 == 0) and (trash < o0):
            po0 = o0
            o0 = trash
        elif (trash % 3 == 0) and (trash < po0):
            po0 = trash
        elif (trash % 3 == 1) and (trash < o1):
            po1 = o1
            o1 = trash
        elif (trash % 3 == 1) and (trash < po1):
            po1 = trash
        elif (trash % 3 == 2) and (trash < o2):
            po2 = o2
            o2 = trash
        elif (trash % 3 == 2) and (trash < po2):
            po2 = trash
    if o0 + o1 < min_summ:
        min_summ = o0 + o1
        mina = o0
        minb = o1

    elif o0 + o2 < min_summ:
        min_summ = o2 + po2
        mina = o0
        minb = o2

    elif o1 + po1 < min_summ:
        min_summ = o1 + po1
        mina = o1
        minb = po1

    elif o2 + po2 < min_summ:
        min_summ = o2 + po2
        mina = o2
        minb = po2

    line[i % 5] = x
print(mina, minb, sep=" ")
"""
 0 + 1 | 0 + 2 | 1 + 1 | 2 + 2 |
"""
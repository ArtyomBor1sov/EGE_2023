f = open('files/35485_A.txt')
N = int(f.readline())
ost_0 = [0, 0, 0]
ost_1 = [0, 0, 0]
ost_2 = [0, 0, 0]
for line in f:
    num = int(line)
    if num % 3 == 0:
        if num > ost_0[0]:
            ost_0[2] = ost_0[1]
            ost_0[1] = ost_0[0]
            ost_0[0] = num
        elif num > ost_0[1]:
            ost_0[2] = ost_0[1]
            ost_0[1] = num
        elif num > ost_0[2]:
            ost_0[2] = num
    elif num % 3 == 1:
        if num > ost_1[0]:
            ost_1[2] = ost_1[1]
            ost_1[1] = ost_1[0]
            ost_1[0] = num
        elif num > ost_1[1]:
            ost_1[2] = ost_1[1]
            ost_1[1] = num
        elif num > ost_1[2]:
            ost_1[2] = num
    else:
        if num > ost_2[0]:
            ost_2[2] = ost_2[1]
            ost_2[1] = ost_2[0]
            ost_2[0] = num
        elif num > ost_2[1]:
            ost_2[2] = ost_2[1]
            ost_2[1] = num
        elif num > ost_2[2]:
            ost_2[2] = num
print(max(sum(ost_0), sum(ost_1), sum(ost_2), ost_0[0] + ost_1[0] + ost_2[0]))

f = open('files/35485_B.txt')
N = int(f.readline())
ost_0 = [0, 0, 0]
ost_1 = [0, 0, 0]
ost_2 = [0, 0, 0]
for line in f:
    num = int(line)
    if num % 3 == 0:
        if num > ost_0[0]:
            ost_0[2] = ost_0[1]
            ost_0[1] = ost_0[0]
            ost_0[0] = num
        elif num > ost_0[1]:
            ost_0[2] = ost_0[1]
            ost_0[1] = num
        elif num > ost_0[2]:
            ost_0[2] = num
    elif num % 3 == 1:
        if num > ost_1[0]:
            ost_1[2] = ost_1[1]
            ost_1[1] = ost_1[0]
            ost_1[0] = num
        elif num > ost_1[1]:
            ost_1[2] = ost_1[1]
            ost_1[1] = num
        elif num > ost_1[2]:
            ost_1[2] = num
    else:
        if num > ost_2[0]:
            ost_2[2] = ost_2[1]
            ost_2[1] = ost_2[0]
            ost_2[0] = num
        elif num > ost_2[1]:
            ost_2[2] = ost_2[1]
            ost_2[1] = num
        elif num > ost_2[2]:
            ost_2[2] = num
print(max(sum(ost_0), sum(ost_1), sum(ost_2), ost_0[0] + ost_1[0] + ost_2[0]))
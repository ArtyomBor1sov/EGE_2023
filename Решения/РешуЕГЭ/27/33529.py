f = open('files/33529_A.txt')
N = int(f.readline())
summa = 0
count_chet = 0
count_nechet = 0
max_chet_1 = 10 ** 12
max_chet_2 = 10 ** 12
max_nechet_1 = 10 ** 12
max_nechet_2 = 10 ** 12
for line in f:
    a, b = sorted([int(x) for x in line.split()])
    summa += b
    if b % 2 == 0:
        count_chet += 1
        if a % 2 != 0:
            if b - a < max_chet_1:
                max_chet_2 = max_chet_1
                max_chet_1 = b - a
            elif b - a < max_chet_2:
                max_chet_2 = b - a
    else:
        count_nechet += 1
        if a % 2 == 0:
            if b - a < max_nechet_1:
                max_nechet_2 = max_nechet_1
                max_nechet_1 = b - a
            elif b - a < max_nechet_2:
                max_nechet_2 = b - a
if summa % 2 == 0 and count_nechet > count_chet:
    if count_nechet - count_chet > 1:
        summa -= min(max_chet_1, max_nechet_1)
    else:
        summa -= min(max_chet_1, max_nechet_1 + max_nechet_2)
elif summa % 2 != 0 and count_chet > count_nechet:
    if count_chet - count_nechet > 1:
        summa -= min(max_chet_1, max_nechet_1)
    else:
        summa -= min(max_chet_1 + max_chet_2, max_nechet_1)
print(summa)

f = open('files/33529_B.txt')
N = int(f.readline())
summa = 0
count_chet = 0
count_nechet = 0
max_chet_1 = 10 ** 12
max_chet_2 = 10 ** 12
max_nechet_1 = 10 ** 12
max_nechet_2 = 10 ** 12
for line in f:
    a, b = sorted([int(x) for x in line.split()])
    summa += b
    if b % 2 == 0:
        count_chet += 1
        if a % 2 != 0:
            if b - a < max_chet_1:
                max_chet_2 = max_chet_1
                max_chet_1 = b - a
            elif b - a < max_chet_2:
                max_chet_2 = b - a
    else:
        count_nechet += 1
        if a % 2 == 0:
            if b - a < max_nechet_1:
                max_nechet_2 = max_nechet_1
                max_nechet_1 = b - a
            elif b - a < max_nechet_2:
                max_nechet_2 = b - a
if summa % 2 == 0 and count_nechet > count_chet:
    if count_nechet - count_chet > 1:
        summa -= min(max_chet_1, max_nechet_1)
    else:
        summa -= min(max_chet_1, max_nechet_1 + max_nechet_2)
elif summa % 2 != 0 and count_chet > count_nechet:
    if count_chet - count_nechet > 1:
        summa -= min(max_chet_1, max_nechet_1)
    else:
        summa -= min(max_chet_1 + max_chet_2, max_nechet_1)
print(summa)
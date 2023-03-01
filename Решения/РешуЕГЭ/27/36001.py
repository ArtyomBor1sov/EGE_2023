f = open('files/36001_A.txt')
N = int(f.readline())
sum_max = 0
sum_min = 0
CN = 10 ** 12
NC = 10 ** 12
NN = 10 ** 12
for line in f:
    a, b = [int(x) for x in line.split()]
    if a % 2 != 0:
        sum_max += max(a, b)
        sum_min += min(a, b)
        if max(a, b) % 2 == 0 and min(a, b) % 2 != 0:
            CN = min(a + b, CN)
        elif max(a, b) % 2 != 0 and min(a, b) % 2 == 0:
            NC = min(a + b, NC)
        elif max(a, b) % 2 != 0 and min(a, b) % 2 != 0:
            NN = min(a + b, NN)
if sum_max % 2 != 0 and sum_min % 2 != 0:
    print(sum_max + sum_min - min(CN, NN + NC))
elif sum_max % 2 == 0 and sum_min % 2 == 0:
    print(sum_max + sum_min - min(NC, NN + CN))
elif sum_max % 2 == 0 and sum_min % 2 != 0:
    print(sum_max + sum_min - min(NN, CN + NC))
else:
    print(sum_max + sum_min)

f = open('files/36001_B.txt')
N = int(f.readline())
sum_max = 0
sum_min = 0
CN = 10 ** 12
NC = 10 ** 12
NN = 10 ** 12
for line in f:
    a, b = [int(x) for x in line.split()]
    if a % 2 != 0:
        sum_max += max(a, b)
        sum_min += min(a, b)
        if max(a, b) % 2 == 0 and min(a, b) % 2 != 0:
            CN = min(a + b, CN)
        elif max(a, b) % 2 != 0 and min(a, b) % 2 == 0:
            NC = min(a + b, NC)
        elif max(a, b) % 2 != 0 and min(a, b) % 2 != 0:
            NN = min(a + b, NN)
if sum_max % 2 != 0 and sum_min % 2 != 0:
    print(sum_max + sum_min - min(CN, NN + NC))
elif sum_max % 2 == 0 and sum_min % 2 == 0:
    print(sum_max + sum_min - min(NC, NN + CN))
elif sum_max % 2 == 0 and sum_min % 2 != 0:
    print(sum_max + sum_min - min(NN, CN + NC))
else:
    print(sum_max + sum_min)
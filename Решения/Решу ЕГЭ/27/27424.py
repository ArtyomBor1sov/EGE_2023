f = open('files/27424_A.txt')
N = int(f.readline())
summa = 0
min_diff = 10 ** 12
for line in f:
    a, b = [int(x) for x in line.split()]
    summa += max(a, b)
    if abs(a - b) % 3 != 0:
        min_diff = min(abs(a - b), min_diff)
if summa % 3 == 0:
    summa -= min_diff
print(summa)

f = open('files/27424_B.txt')
N = int(f.readline())
summa = 0
min_diff = 10 ** 12
for line in f:
    a, b = [int(x) for x in line.split()]
    summa += max(a, b)
    if abs(a - b) % 3 != 0:
        min_diff = min(abs(a - b), min_diff)
if summa % 3 == 0:
    summa -= min_diff
print(summa)
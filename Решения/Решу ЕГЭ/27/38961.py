f = open('files/38961_A.txt')
N = int(f.readline())
summa = 0
max_summa = 0
counter = 0
data = {}
for line in f:
    num = int(line)
    summa += num
    if num % 2 == 0:
        counter += 1
    if counter % 10 == 0:
        max_summa = summa
    else:
        if counter % 10 in data:
            max_summa = max(summa - data[counter % 10], max_summa)
        else:
            data[counter % 10] = summa
print(max_summa)

f = open('files/38961_B.txt')
N = int(f.readline())
summa = 0
max_summa = 0
counter = 0
data = {}
for line in f:
    num = int(line)
    summa += num
    if num % 2 == 0:
        counter += 1
    if counter % 10 == 0:
        max_summa = summa
    else:
        if counter % 10 in data:
            max_summa = max(summa - data[counter % 10], max_summa)
        else:
            data[counter % 10] = summa
print(max_summa)
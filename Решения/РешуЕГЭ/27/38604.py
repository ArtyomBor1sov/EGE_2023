f = open('files/38604_A.txt')
N = int(f.readline())
summa = 0
max_summa = 0
counter = 0
min_counter = 0
data = {}
for line in f:
    num = int(line)
    summa += num
    counter += 1
    if summa % 43 == 0:
        if summa > max_summa:
            max_summa = summa
            min_counter = counter
        elif summa == max_summa:
            min_counter = min(counter, min_counter)
    else:
        if summa % 43 in data:
            if summa - data[summa % 43][0] > max_summa:
                max_summa = summa - data[summa % 43][0]
                min_counter = counter - data[summa % 43][1]
            elif summa - data[summa % 43][0] == max_summa:
                min_counter = min(counter - data[summa % 43][1], min_counter)
        else:
            data[summa % 43] = [summa, counter]
print(min_counter)

f = open('files/38604_B.txt')
N = int(f.readline())
summa = 0
max_summa = 0
counter = 0
min_counter = 0
data = {}
for line in f:
    num = int(line)
    summa += num
    counter += 1
    if summa % 43 == 0:
        if summa > max_summa:
            max_summa = summa
            min_counter = counter
        elif summa == max_summa:
            min_counter = min(counter, min_counter)
    else:
        if summa % 43 in data:
            if summa - data[summa % 43][0] > max_summa:
                max_summa = summa - data[summa % 43][0]
                min_counter = counter - data[summa % 43][1]
            elif summa - data[summa % 43][0] == max_summa:
                min_counter = min(counter - data[summa % 43][1], min_counter)
        else:
            data[summa % 43] = [summa, counter]
print(min_counter)
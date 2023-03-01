from math import *

f = open('files/33105.txt')
N = int(f.readline())
data = []
summa = 0
for line in f:
    if int(line) > 100:
        data.append(int(line))
    else:
        summa += int(line)
data.sort()
for i in range(len(data) // 2):
    summa += data[i] * 0.7
    maximum = data[i]
for i in range(len(data) // 2, len(data)):
    summa += data[i]
print(ceil(summa), maximum)
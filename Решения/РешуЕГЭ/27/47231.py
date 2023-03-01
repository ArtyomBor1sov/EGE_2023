from math import *

f = open('files/47231_A.txt')
N = int(f.readline())
data = []
summa = 0
left = 0
right = 0
for line in f:
    place, amount = [int(x) for x in line.split()]
    amount = ceil(amount / 36)
    data.append([place, amount])
    summa += amount * (place - data[0][0])
    right += amount
minimum = summa
for i in range(1, N):
    left += data[i - 1][1]
    right -= data[i - 1][1]
    summa += (left - right) * (data[i][0] - data[i - 1][0])
    minimum = min(summa, minimum)
print(minimum)

f = open('files/47231_B.txt')
N = int(f.readline())
data = []
summa = 0
left = 0
right = 0
for line in f:
    place, amount = [int(x) for x in line.split()]
    amount = ceil(amount / 36)
    data.append([place, amount])
    summa += amount * (place - data[0][0])
    right += amount
minimum = summa
for i in range(1, N):
    left += data[i - 1][1]
    right -= data[i - 1][1]
    summa += (left - right) * (data[i][0] - data[i - 1][0])
    minimum = min(summa, minimum)
print(minimum)
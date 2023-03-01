f = open('files/46985_A.txt')
N = int(f.readline())
summa = 0
counter = 0
data = {0: 1}
for line in f:
    summa += int(line)
    counter += data.get(summa % 999, 0)
    data[summa % 999] = data.get(summa % 999, 0) + 1
print(counter)

f = open('files/46985_B.txt')
N = int(f.readline())
summa = 0
counter = 0
data = {0: 1}
for line in f:
    summa += int(line)
    counter += data.get(summa % 999, 0)
    data[summa % 999] = data.get(summa % 999, 0) + 1
print(counter)
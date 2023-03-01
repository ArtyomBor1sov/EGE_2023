f = open('files/33198.txt')
N, M = [int(x) for x in f.readline().split()]
summa = 0
counter = 0
data = []
for line in f:
    if 200 <= int(line) <= 210:
        summa += int(line)
        counter += 1
    else:
        data.append(int(line))
data.sort()
for i in range(N):
    if summa + data[i] <= M:
        summa += data[i]
        counter += 1
    else:
        break
end = N
for i in range(counter - 1, -1, -1):
    for j in range(i, end):
        if summa + data[j] - data[i] <= M:
            end = j
            diff = data[j] - data[i]
        else:
            break
    summa += diff
print(counter, summa)
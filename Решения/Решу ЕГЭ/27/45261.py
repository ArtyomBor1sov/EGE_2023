f = open('files/45261_A.txt')
N = int(f.readline())
data = []
for line in f:
    data.append(int(line))
summa = 0
minus = 0
plus = 0
for i in range(N):
    summa += data[i] * 3 * min(i, N - i)
    if i < N // 2:
        minus += data[i]
    else:
        plus += data[i]
minimum = summa
for i in range(1, N):
    minus += data[(i + N // 2 - 1) % N]
    minus -= data[i - 1]
    plus += data[i - 1]
    plus -= data[(i + N // 2 - 1) % N]
    summa += 3 * (plus - minus)
    minimum = min(summa, minimum)
print(minimum)

f = open('files/45261_B.txt')
N = int(f.readline())
data = []
for line in f:
    data.append(int(line))
summa = 0
minus = 0
plus = 0
for i in range(N):
    summa += data[i] * 3 * min(i, N - i)
    if i < N // 2:
        minus += data[i]
    else:
        plus += data[i]
minimum = summa
for i in range(1, N):
    minus += data[(i + N // 2 - 1) % N]
    minus -= data[i - 1]
    plus += data[i - 1]
    plus -= data[(i + N // 2 - 1) % N]
    summa += 3 * (plus - minus)
    minimum = min(summa, minimum)
print(minimum)
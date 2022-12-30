f = open('../files/27-A.txt', 'r')
N = int(f.readline())
data = [[0] * 11 for i in range(3)]
for line in f:
    num = int(line)
    degree = 0
    while num % 2 ** (degree + 1) == 0:
        degree += 1
    degree = min(degree, 10)
    ostatok = num % 3
    data[ostatok][degree] += 1
counter = 0
for i in range(11):
    for j in range(i, 11):
        if (i + j) >= 10:
            if i < j:
                counter += data[0][i] * data[0][j] + data[1][i] * data[2][j] + data[1][j] * data[2][i]
            else:
                counter += data[0][i] * (data[0][i] - 1) // 2 + data[1][i] * data[2][i]
print(counter)

f = open('../files/27-B.txt', 'r')
N = int(f.readline())
data = [[0] * 11 for i in range(3)]
for line in f:
    num = int(line)
    degree = 0
    while num % 2 ** (degree + 1) == 0:
        degree += 1
    degree = min(degree, 10)
    ostatok = num % 3
    data[ostatok][degree] += 1
counter = 0
for i in range(11):
    for j in range(i, 11):
        if (i + j) >= 10:
            if i < j:
                counter += data[0][i] * data[0][j] + data[1][i] * data[2][j] + data[1][j] * data[2][i]
            else:
                counter += data[0][i] * (data[0][i] - 1) // 2 + data[1][i] * data[2][i]
print(counter)
f = open('../files/27-B.txt', 'r')
N = int(f.readline())
data = [[0] * 9 for i in range(4)]
for line in f:
    num = int(line)
    ostatok = num % 4
    stepen = 0
    while num % 3 == 0:
        num = num // 3
        stepen += 1
    stepen = min(stepen, 8)
    data[ostatok][stepen] += 1
counter = 0
for i in range(9):
    for j in range(i, 9):
        if i + j >= 8:
            if i == j:
                counter += data[0][i] * (data[0][i] - 1) // 2 + data[1][i] * data[3][i] + data[2][i] * (data[2][i] - 1) // 2
            else:
                counter += data[0][i] * data[0][j] + data[1][i] * data[3][j] + data[1][j] * data[3][i] + data[2][i] * data[2][j]
print(counter)
f = open('files/37161.txt')
N = int(f.readline())
data = []
for line in f:
    data.append([int(x) for x in line.split()])
data.sort()
max_row = 0
for i in range(N - 1):
    if data[i][0] == data[i + 1][0] and data[i + 1][1] - data[i][1] == 3 and data[i][0] > max_row:
        max_row = data[i][0]
        min_place = data[i][1] + 1
print(max_row, min_place)
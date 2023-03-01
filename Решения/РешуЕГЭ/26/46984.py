f = open('files/46984.txt')
N = int(f.readline())
data = [[False] * 10000 for i in range(10000)]
data[0][0] = True
for line in f:
    row, place = [int(x) for x in line.split()]
    data[row - 1][place - 1] = True
maximum = 0
for i in range(10000):
    counter = 0
    for j in range(10000):
        if data[i][j]:
            counter += 1
            if counter > maximum:
                maximum = counter
                min_row = i + 1
        else:
            counter = 0
print(maximum, min_row)
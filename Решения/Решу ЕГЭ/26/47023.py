f = open('files/47023.txt')
N = int(f.readline())
data = [[False] * 10000 for i in range(10000)]
data[0][0] = True
for line in f:
    row, place = [int(x) for x in line.split()]
    data[row - 1][place - 1] = True
maximum = 0
for i in range(10000):
    counter = 0
    j = 0
    while j < 10000:
        if data[i][j] and (counter == 0 or not data[i][j - 1]):
            counter += 1
            if counter > maximum:
                maximum = counter
                min_row = i + 1
            j += 2
        else:
            counter = 0
            j += 1
print(maximum, min_row)
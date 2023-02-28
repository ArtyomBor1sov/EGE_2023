f = open('files/47023.txt')
N = int(f.readline())
data = []
for line in f:
    data.append([int(x) for x in line.split()])
data.sort()
counter = 1
maximum = 1
for i in range(1, len(data)):
    if data[i][0] == data[i - 1][0] and data[i][1] - data[i - 1][1] == 2:
        counter += 1
        if counter > maximum:
            maximum = counter
            max_row = data[i][0]
    elif data[i][0] != data[i - 1][0] or data[i][1] != data[i - 1][1]:
        counter = 1
print(maximum, max_row)
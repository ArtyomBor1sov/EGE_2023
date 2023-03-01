f = open('../files/26.txt')
N = int(f.readline())
data = []
for line in f:
    data.append([int(x) for x in line.split()])
data.sort()
curr_len = 1
counter = 0
maximum = 0
for i in range(1, N):
    if data[i][0] == data[i - 1][0]:
        if data[i][1] - data[i - 1][1] == 1:
            curr_len += 1
        elif data[i][1] != data[i - 1][1]:
            if curr_len >= 3:
                counter += 1
            curr_len = 1
    else:
        if curr_len >= 3:
            counter += 1
        curr_len = 1
        if counter >= maximum:
            maximum = counter
            max_row = data[i - 1][0]
        counter = 0
if counter >= maximum:
    maximum = counter
    max_row = data[-1][0]
print(maximum, max_row)
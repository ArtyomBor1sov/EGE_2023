f = open('files/39255.txt')
N, M = [int(x) for x in f.readline().split()]
data = []
for line in f:
    price, kind = line.split()
    data.append([int(price), kind])
data.sort()
counter = 0
for i in range(N):
    if data[i][0] <= M:
        M -= data[i][0]
        last_ind = i
        if data[i][1] == 'B':
            counter += 1
    else:
        break
start = last_ind + 1
for i in range(last_ind, -1, -1):
    if data[i][1] == 'A':
        for j in range(start, N):
            if data[j][1] == 'B' and data[j][0] - data[i][0] <= M:
                M -= (data[j][0] - data[i][0])
                counter += 1
                start = j + 1
                break
        else:
            break
print(counter, M)
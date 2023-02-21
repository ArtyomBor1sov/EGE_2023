f = open('files/36039.txt')
S, N = [int(x) for x in f.readline().split()]
data = []
for line in f:
    data.append(int(line))
data.sort()
counter = 0
for i in range(N):
    if data[i] <= S:
        S -= data[i]
        counter += 1
    else:
        break
for i in range(counter - 1, N):
    if data[i] - data[counter - 1] <= S:
        maximum = data[i]
    else:
        break
print(counter, maximum)
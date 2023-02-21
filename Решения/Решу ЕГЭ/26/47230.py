f = open('files/47230.txt')
N = int(f.readline())
data = []
for line in f:
    data.append(int(line))
data.sort(reverse = True)
counter = 1
last_box = 0
for i in range(1, N):
    if data[last_box] - data[i] >= 3:
        counter += 1
        last_box = i
print(counter, data[last_box])
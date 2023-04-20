f = open('files/5028_A.txt')
N, K = [int(x) for x in f.readline().split()]
data = [int(line) for line in f]
indices = {}
minimum = N
for i in range(N):
    indices[data[i]] = i
    if len(indices) == K:
        minimum = min(i - min(indices.values()) + 1, minimum)
print(minimum)

f = open('files/5028_B.txt')
N, K = [int(x) for x in f.readline().split()]
data = [int(line) for line in f]
indices = {}
minimum = N
for i in range(N):
    indices[data[i]] = i
    if len(indices) == K:
        minimum = min(i - min(indices.values()) + 1, minimum)
print(minimum)
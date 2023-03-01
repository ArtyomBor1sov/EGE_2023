f = open('files/5311_A.txt')
N = int(f.readline())
data = {}
for line in f:
    data[int(line)] = data.get(int(line), 0) + 1
pair = 0
unique = 0
for key, val in data.items():
    if val >= 2:
        pair += 1
    else:
        unique += 1
print((pair * 2 + unique + 1) // 2)

f = open('files/5311_B.txt')
N = int(f.readline())
data = {}
for line in f:
    data[int(line)] = data.get(int(line), 0) + 1
pair = 0
unique = 0
for key, val in data.items():
    if val >= 2:
        pair += 1
    else:
        unique += 1
print((pair * 2 + unique + 1) // 2)
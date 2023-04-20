f = open('files/5177-A.txt')
N = int(f.readline())
data = []
for line in f:
    data.append([int(x) for x in line.split()])
data.sort()
i = 1
while i < len(data):
    if data[i][0] <= data[i - 1][0]:
        data.pop(i)
    else:
        while i > 0 and data[i][1] <= data[i - 1][1]:
            data.pop(i - 1)
            i -= 1
        i += 1
i = 1
while i < len(data):
    if data[i][0] <= data[i - 1][1]:
        data.pop(i)
    else:
        i += 1
print(len(data))

f = open('files/5177-B.txt')
N = int(f.readline())
data = []
for line in f:
    data.append([int(x) for x in line.split()])
data.sort()
i = 1
while i < len(data):
    if data[i][0] <= data[i - 1][0]:
        data.pop(i)
    else:
        while i > 0 and data[i][1] <= data[i - 1][1]:
            data.pop(i - 1)
            i -= 1
        i += 1
i = 1
while i < len(data):
    if data[i][0] <= data[i - 1][1]:
        data.pop(i)
    else:
        i += 1
print(len(data))
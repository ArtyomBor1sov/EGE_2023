f = open('files/36037.txt')
parts = f.readline().split('XZZY')
maximum = 0
for i in range(len(parts)):
    if i == 0 or i == len(parts) - 1:
        maximum = max(len(parts[i]) + 3, maximum)
    else:
        maximum = max(len(parts[i]) + 6, maximum)
print(maximum)
f = open('files/36037.txt', 'r')
line = f.readline()
counter = 3
maximum = 3
for i in range(3, len(line)):
    if line[i] != 'Y' or line[i - 3:i] != 'XZZ':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 3
print(maximum)
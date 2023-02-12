f = open('files/27421.txt', 'r')
line = f.readline()
counter = 1
maximum = 1
for i in range(1, len(line)):
    if line[i] != line[i - 1]:
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 1
print(maximum)
f = open('files/45258.txt')
line = f.readline()
counter = 0
maximum = 0
i = 0
while i < len(line):
    if line[i] in 'AC' and line[i + 1] == 'B':
        counter += 1
        maximum = max(counter, maximum)
        i += 2
    else:
        counter = 0
        i += 1
print(maximum)
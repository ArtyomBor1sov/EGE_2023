f = open('../files/24.txt', 'r')
maximum = 0
for line in f:
    counter = 1
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            counter += 1
            if counter > maximum:
                maximum = counter
                answer = line.count(line[i])
            elif counter >= maximum:
                answer = max(line.count(line[i]), answer)
        else:
            counter = 1
print(answer)
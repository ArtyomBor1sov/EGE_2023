f = open('../files/24.txt')
maximum = 0
max_lines = []
for line in f:
    counter = 1
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            counter += 1
            if counter > maximum:
                maximum = counter
                max_lines = [[line, line[i]]]
            elif counter == maximum:
                max_lines.append([line, line[i]])
        else:
            counter = 1
answer = 0
for line, letter in max_lines:
    answer = max(line.count(letter), answer)
print(answer)
f = open('files/27689.txt', 'r')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if ((symbol == 'X' and counter % 3 == 0) or
        (symbol == 'Y' and counter % 3 == 1) or
        (symbol == 'Z' and counter % 3 == 2)):
        counter += 1
        maximum = max(counter, maximum)
    else:
        if symbol == 'X':
            counter = 1
        else:
            counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('XYZ' * 4 + 'X'))
# print(line.count('XYZ' * 4 + 'XY'))
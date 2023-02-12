f = open('files/27694.txt', 'r')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if ((symbol == 'A' and counter % 2 == 0) or
        (symbol == 'B' and counter % 2 == 1)):
        counter += 1
        maximum = max(counter, maximum)
    else:
        if symbol == 'A':
            counter = 1
        else:
            counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('AB' * 12))
# print(line.count('AB' * 12 + 'A'))
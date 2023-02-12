f = open('files/27699.txt', 'r')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if ((symbol == 'L' and counter % 3 == 0) or
        (symbol == 'D' and counter % 3 == 1) or
        (symbol == 'R' and counter % 3 == 2)):
        counter += 1
        maximum = max(counter, maximum)
    else:
        if symbol == 'L':
            counter = 1
        else:
            counter = 0        
print(maximum)

# ПРОВЕРКА
# print(line.count('LDR' * 5))
# print(line.count('LDR' * 5 + 'L'))
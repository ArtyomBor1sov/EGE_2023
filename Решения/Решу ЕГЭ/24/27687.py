f = open('files/27687.txt')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if symbol == 'Y':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('Y' * 10))
# print(line.count('Y' * 11))
f = open('files/27686.txt')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if symbol == 'X':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('X' * 19))
# print(line.count('X' * 20))
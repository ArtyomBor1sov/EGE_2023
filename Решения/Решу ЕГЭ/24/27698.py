f = open('files/27698.txt')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if symbol == 'R':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('R' * 1))
# print(line.count('R' * 2))
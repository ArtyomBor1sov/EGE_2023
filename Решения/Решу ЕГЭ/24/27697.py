f = open('files/27697.txt')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if symbol == 'D':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('D' * 11))
# print(line.count('D' * 12))
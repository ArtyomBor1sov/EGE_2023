f = open('files/27692.txt')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if symbol == 'B':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('B' * 11))
# print(line.count('B' * 12))
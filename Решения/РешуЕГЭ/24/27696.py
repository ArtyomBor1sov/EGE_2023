f = open('files/27696.txt')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if symbol == 'L':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('L' * 7))
# print(line.count('L' * 8))
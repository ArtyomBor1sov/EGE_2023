f = open('files/27688.txt')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if symbol == 'Z':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('Z' * 7))
# print(line.count('Z' * 8))
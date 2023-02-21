f = open('files/27693.txt')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if symbol == 'C':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('C' * 1))
# print(line.count('C' * 2))
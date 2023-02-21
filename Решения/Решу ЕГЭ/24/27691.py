f = open('files/27691.txt')
line = f.readline()
counter = 0
maximum = 0
for symbol in line:
    if symbol == 'A':
        counter += 1
        maximum = max(counter, maximum)
    else:
        counter = 0
print(maximum)

# ПРОВЕРКА
# print(line.count('A' * 7))
# print(line.count('A' * 8))
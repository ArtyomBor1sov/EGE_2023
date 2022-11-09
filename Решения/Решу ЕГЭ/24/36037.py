f = open('files/36037.txt', 'r')
stroka = f.readline()
counter = 3
maximum = 3
for i in range(3, len(stroka)):
    if stroka[i] != 'Y' or stroka[i - 3:i] != 'XZZ':
        counter += 1
    else:
        maximum = max(counter, maximum)
        counter = 3
maximum = max(counter, maximum)
print(maximum)
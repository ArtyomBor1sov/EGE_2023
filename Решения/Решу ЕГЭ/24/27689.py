f = open('files/27689.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
for i in range(len(stroka)):
    if ((stroka[i] == 'X' and counter % 3 == 0) or
        (stroka[i] == 'Y' and counter % 3 == 1) or
        (stroka[i] == 'Z' and counter % 3 == 2)):
        counter += 1
    else:
        maximum = max(counter, maximum)
        if stroka[i] == 'X':
            counter = 1
        else:
            counter = 0
maximum = max(counter, maximum)
print(maximum)
#ПРОВЕРКА
print(stroka.count('XYZ' * 4 + 'X'))
print(stroka.count('XYZ' * 4 + 'XY'))

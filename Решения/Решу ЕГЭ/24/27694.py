f = open('files/27694.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
for i in range(len(stroka)):
    if ((stroka[i] == 'A' and counter % 2 == 0) or
        (stroka[i] == 'B' and counter % 2 == 1)):
        counter += 1
    else:
        maximum = max(counter, maximum)
        if stroka[i] == 'A':
            counter = 1
        else:
            counter = 0
maximum = max(counter, maximum)
print(maximum)
#ПРОВЕРКА
print(stroka.count('AB' * 12))
print(stroka.count('AB' * 12 + 'A'))

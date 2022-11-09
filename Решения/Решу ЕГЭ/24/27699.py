f = open('files/27699.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
for i in range(len(stroka)):
    if ((stroka[i] == 'L' and counter % 3 == 0) or
        (stroka[i] == 'D' and counter % 3 == 1) or
        (stroka[i] == 'R' and counter % 3 == 2)):
        counter += 1
    else:
        maximum = max(counter, maximum)
        if stroka[i] == 'L':
            counter = 1
        else:
            counter = 0        
maximum = max(counter, maximum)
print(maximum)
#ПРОВЕРКА
print(stroka.count('LDR' * 5))
print(stroka.count('LDR' * 5 + 'L'))

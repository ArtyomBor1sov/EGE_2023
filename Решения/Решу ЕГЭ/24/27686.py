f = open('files/27686.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
for i in range(len(stroka)):
    if stroka[i] == 'X':
        counter += 1
    else:
        maximum = max(counter, maximum)
        counter = 0
maximum = max(counter, maximum)
print(maximum)
#ПРОВЕРКА
print(stroka.count('X' * 19))
print(stroka.count('X' * 20))

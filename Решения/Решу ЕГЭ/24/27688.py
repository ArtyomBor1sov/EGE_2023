f = open('files/27688.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
for i in range(len(stroka)):
    if stroka[i] == 'Z':
        counter += 1
    else:
        maximum = max(counter, maximum)
        counter = 0
maximum = max(counter, maximum)
print(maximum)
#ПРОВЕРКА
print(stroka.count('Z' * 7))
print(stroka.count('Z' * 8))

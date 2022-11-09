f = open('files/27692.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
for i in range(len(stroka)):
    if stroka[i] == 'B':
        counter += 1
    else:
        maximum = max(counter, maximum)
        counter = 0
maximum = max(counter, maximum)
print(maximum)
#ПРОВЕРКА
print(stroka.count('B' * 11))
print(stroka.count('B' * 12))

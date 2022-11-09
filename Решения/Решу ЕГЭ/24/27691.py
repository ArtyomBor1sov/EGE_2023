f = open('files/27691.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
for i in range(len(stroka)):
    if stroka[i] == 'A':
        counter += 1
    else:
        maximum = max(counter, maximum)
        counter = 0
maximum = max(counter, maximum)
print(maximum)
#ПРОВЕРКА
print(stroka.count('A' * 7))
print(stroka.count('A' * 8))

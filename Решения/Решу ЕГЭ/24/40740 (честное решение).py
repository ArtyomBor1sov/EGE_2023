f = open('files/40740.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
counter_E = 0
for i in range(len(stroka)):
    if stroka[i] != 'A':
        counter += 1
        if stroka[i] == 'E':
            counter_E += 1
    else:
        if counter_E >= 3:
            maximum = max(counter, maximum)
        counter = 0
        counter_E = 0
if counter_E >= 3:
    maximum = max(counter, maximum)
print(maximum)
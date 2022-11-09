f = open('files/37131.txt', 'r')
stroka = f.readline()
counter = 1
maximum = 1
for i in range(1, len(stroka)):
    if stroka[i - 1:i + 1] != 'KL' and stroka[i - 1:i + 1] != 'LK':
        counter += 1
    else:
        maximum = max(counter, maximum)
        counter = 1
maximum = max(counter, maximum)
print(maximum)
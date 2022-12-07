f = open('../files/24.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
i = 0
while i < len(stroka) - 2:
    if stroka[i] in 'CDF' and stroka[i + 1] in 'CDF' and stroka[i + 2] in 'AO':
        counter += 1
        i += 3
    else:
        maximum = max(counter, maximum)
        counter = 0
        i += 1
maximum = max(counter, maximum)
print(maximum)
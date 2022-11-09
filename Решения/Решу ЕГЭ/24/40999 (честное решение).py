f = open('files/40999.txt', 'r')
stroka = f.readline()
counter = 0
maximum = 0
counter_A = 0
for i in range(len(stroka)):
    if stroka[i] != 'E':
        counter += 1
        if stroka[i] == 'A':
            counter_A += 1
    else:
        if counter_A >= 3:
            maximum = max(counter, maximum)
        counter = 0
        counter_A= 0
if counter_A >= 3:
    maximum = max(counter, maximum)
print(maximum)
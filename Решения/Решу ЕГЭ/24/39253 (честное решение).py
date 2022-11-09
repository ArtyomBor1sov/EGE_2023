f = open('files/39253.txt', 'r')
stroka = f.readline()
start = 0
finish = 0
count_D = 0
maximum = 0
for i in range(len(stroka)):
    if stroka[i] != 'D':
         finish = i
    else:
        if count_D == 0:
            count_D += 1
        else:
            maximum = max(finish - start + 1, maximum)
            start = prev_D + 1
        finish = i
        prev_D = i
maximum = max(finish - start + 1, maximum)
print(maximum)
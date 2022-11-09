f = open('files/38958.txt', 'r')
stroka = f.readline()
start = 0
finish = 0
count_A = 0
maximum = 0
for i in range(len(stroka)):
    if stroka[i] != 'A':
         finish = i
    else:
        if count_A == 0:
            count_A += 1
        else:
            maximum = max(finish - start + 1, maximum)
            start = prev_A + 1
        finish = i
        prev_A = i
maximum = max(finish - start + 1, maximum)
print(maximum)

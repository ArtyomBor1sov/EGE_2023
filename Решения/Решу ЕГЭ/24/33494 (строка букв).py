f = open('files/33494.txt', 'r')
stroka = f.readline()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter = [0] * 26
for i in range(1, len(stroka)):
    if stroka[i - 1] == 'E':
        counter[letters.find(stroka[i])] += 1
max_ind = 0
for i in range(len(counter)):
    if counter[i] > counter[max_ind]:
        max_ind = i
print(letters[max_ind])
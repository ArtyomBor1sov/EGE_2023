f = open('files/33769.txt', 'r')
stroka = f.readline()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter = [0] * 26
for i in range(2, len(stroka)):
    if stroka[i - 1] == stroka[i - 2]:
        counter[letters.find(stroka[i])] += 1
max_ind = 0
for i in range(len(counter)):
    if counter[i] > counter[max_ind]:
        max_ind = i
print(letters[max_ind])
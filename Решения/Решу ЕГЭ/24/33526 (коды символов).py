f = open('files/33526.txt', 'r')
stroka = f.readline()
counter = [0] * 26
for i in range(1, len(stroka) - 1):
    if stroka[i - 1] == stroka[i + 1]:
        counter[ord(stroka[i]) - ord('A')] += 1
max_ind = 0
for i in range(len(counter)):
    if counter[i] > counter[max_ind]:
        max_ind = i
print(chr(ord('A') + max_ind))
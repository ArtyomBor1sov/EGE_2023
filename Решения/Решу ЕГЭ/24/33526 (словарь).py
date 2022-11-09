f = open('files/33526.txt', 'r')
stroka = f.readline()
counter = {}
for i in range(1, len(stroka) - 1):
    if stroka[i - 1] == stroka[i + 1]:
        counter[stroka[i]] = counter.get(stroka[i], 0) + 1
maximum = 0
for key, val in counter.items():
    if val > maximum:
        maximum = val
        max_letter = key
print (max_letter)
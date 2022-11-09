f = open('files/38602.txt', 'r')
stroka = f.readline()
stroka = stroka.replace('PP', 'P P')
words = stroka.split()
maximum = 0
for i in range(len(words)):
    maximum = max(len(words[i]), maximum)
print(maximum)
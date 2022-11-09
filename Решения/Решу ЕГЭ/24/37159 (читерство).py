f = open('files/37159.txt', 'r')
stroka = f.readline()
stroka = stroka.replace('ad', 'a d')
stroka = stroka.replace('da', 'd a')
words = stroka.split()
maximum = 0
for i in range(len(words)):
    maximum = max(len(words[i]), maximum)
print(maximum)
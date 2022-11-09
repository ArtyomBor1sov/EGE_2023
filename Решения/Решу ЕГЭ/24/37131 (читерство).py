f = open('files/37131.txt', 'r')
stroka = f.readline()
stroka = stroka.replace('KL', 'K L')
stroka = stroka.replace('LK', 'L K')
words = stroka.split()
maximum = 0
for i in range(len(words)):
    maximum = max(len(words[i]), maximum)
print(maximum)
f = open('files/40740.txt', 'r')
words = f.readline().split('A')
maximum = 0
for i in range(len(words)):
    if words[i].count('E') >= 3:
        maximum = max(len(words[i]), maximum)
print(maximum)
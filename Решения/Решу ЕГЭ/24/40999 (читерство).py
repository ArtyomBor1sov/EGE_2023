f = open('files/40999.txt', 'r')
words = f.readline().split('E')
maximum = 0
for i in range(len(words)):
    if words[i].count('A') >= 3:
        maximum = max(len(words[i]), maximum)
print(maximum)
f = open('files/38958.txt', 'r')
words = f.readline().split('A')
maximum = 0
for i in range(len(words) - 1):
    maximum = max(len(words[i]) + len(words[i + 1]) + 1, maximum)
print(maximum)

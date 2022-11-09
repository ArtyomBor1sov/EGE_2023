f = open('files/39253.txt', 'r')
words = f.readline().split('D')
maximum = 0
for i in range(1, len(words)):
    maximum = max(len(words[i]) + len(words[i - 1]) + 1, maximum)
print(maximum)
f = open('files/35998.txt', 'r')
maximum = 0
for line in f:
    if line.count('A') < 25:
        for code in range(ord('A'), ord('Z') + 1):
            maximum = max(line.rfind(chr(code)) - line.find(chr(code)), maximum)
print(maximum)
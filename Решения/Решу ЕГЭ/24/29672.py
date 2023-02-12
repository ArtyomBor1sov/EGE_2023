f = open('files/29672.txt', 'r')
counter = 0
for line in f:
    if line.count('E') > line.count('A'):
        counter += 1
print(counter)
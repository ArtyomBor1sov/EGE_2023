f = open('files/33103.txt')
counter = 0
for line in f:
    if line.count('A') > line.count('E'):
        counter += 1
print(counter)
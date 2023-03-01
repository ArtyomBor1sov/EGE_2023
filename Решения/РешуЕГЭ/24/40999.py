f = open('files/40999.txt')
parts = f.readline().split('E')
maximum = 0
for element in parts:
    if element.count('A') >= 3:
        maximum = max(len(element), maximum)
print(maximum)
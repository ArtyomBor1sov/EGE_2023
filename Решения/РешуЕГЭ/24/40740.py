f = open('files/40740.txt')
parts = f.readline().split('A')
maximum = 0
for element in parts:
    if element.count('E') >= 3:
        maximum = max(len(element), maximum)
print(maximum)
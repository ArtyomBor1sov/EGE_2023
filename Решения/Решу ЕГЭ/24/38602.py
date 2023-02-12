f = open('files/38602.txt', 'r')
line = f.readline()
line = line.replace('PP', 'P P')
parts = line.split()
maximum = 0
for element in parts:
    maximum = max(len(element), maximum)
print(maximum)
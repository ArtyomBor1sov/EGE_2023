f = open('files/37159.txt')
line = f.readline()
line = line.replace('ad', 'a d')
line = line.replace('da', 'd a')
parts = line.split()
maximum = 0
for element in parts:
    maximum = max(len(element), maximum)
print(maximum)
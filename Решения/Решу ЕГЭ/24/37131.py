f = open('files/37131.txt', 'r')
line = f.readline()
line = line.replace('KL', 'K L')
line = line.replace('LK', 'L K')
parts = line.split()
maximum = 0
for element in parts:
    maximum = max(len(element), maximum)
print(maximum)
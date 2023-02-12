f = open('files/38958.txt', 'r')
parts = f.readline().split('A')
maximum = 0
for i in range(len(parts) - 1):
    maximum = max(len(parts[i]) + len(parts[i + 1]) + 1, maximum)
print(maximum)
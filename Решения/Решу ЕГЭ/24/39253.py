f = open('files/39253.txt')
parts = f.readline().split('D')
maximum = 0
for i in range(1, len(parts)):
    maximum = max(len(parts[i]) + 1 + len(parts[i - 1]), maximum)
print(maximum)
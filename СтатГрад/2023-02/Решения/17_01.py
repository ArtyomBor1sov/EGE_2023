f = open('../files/17.txt')
data = []
minimum = 10000
for line in f:
    data.append(int(line))
    if abs(int(line)) % 10 == 3:
        minimum = min(int(line), minimum)
counter = 0
maximum = 0
for i in range(len(data) - 1):
    if ((abs(data[i]) % 10 == abs(data[i + 1]) % 10)
            and ((data[i] % 3 == 0 and data[i + 1] % 3 != 0) or (data[i + 1] % 3 == 0 and data[i] % 3 != 0))
            and (data[i] ** 2 + data[i + 1] ** 2 <= minimum ** 2)):
        counter += 1
        maximum = max(data[i] ** 2 + data[i + 1] ** 2, maximum)
print(counter, maximum)
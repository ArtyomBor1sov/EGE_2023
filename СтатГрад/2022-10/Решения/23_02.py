data = [0] * 61
data[1] = 1
for i in range(2, 61):
    if str(i).count('5') == 0:
        data[i] = data[i - 1]
        if i % 2 == 0 and i // 2 >= 1:
            data[i] += data[i // 2]
print(data[60])
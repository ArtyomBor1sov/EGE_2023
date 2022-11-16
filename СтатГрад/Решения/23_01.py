data = [0] * 41
data[1] = 1
for i in range(2, 41):
    if str(i).count('3') > 0:
        data[i] = 0
    else:
        data[i] = data[i - 1]
        if i % 2 == 0 and i // 2 >= 1:
            data[i] += data[i // 2]
print(data[40])
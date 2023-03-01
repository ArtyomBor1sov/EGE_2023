counter = 0
for i in range(11):
    for j in range(i + 2, 11):
        for k in range(j + 2, 11):
            if i == 0:
                counter += 4 ** 11
            else:
                counter += 3 * 4 ** 10
print(counter)
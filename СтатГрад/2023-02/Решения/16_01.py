counter = 0
for div in range(1, int(1048576 ** 0.5) + 1):
    if 1048576 % div == 0:
        counter += 1
        if div != 1048576 // div:
            counter += 1
print(counter)
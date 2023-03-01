k = 0
for num in range(2422000, 2422081):
    counter = 0
    for div in range(2, num):
        if num % div == 0:
            counter += 1
            break
    if counter == 0:
        k += 1
        print(k, num)
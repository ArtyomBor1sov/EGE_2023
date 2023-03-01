for num in range(1000000, 2000001):
    counter = 0
    for div in range(int(num ** 0.5), 949, -1):
        if num % div == 0:
            if num // div - div <= 100:
                counter += 1
            else:
                break
    if counter >= 3:
        print(num)
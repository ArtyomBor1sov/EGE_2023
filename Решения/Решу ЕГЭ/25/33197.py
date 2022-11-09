for num in range(1000000, 2000001):
    counter = 0
    good_counter = 0
    for div in range(int(num ** (1 / 2)), 949, -1):
        if num % div == 0:
            counter += 1
            if num // div - div <= 100:
                good_counter += 1
            if counter == 3 or num // div - div > 100:
                break
    if good_counter == 3:
        print(num)
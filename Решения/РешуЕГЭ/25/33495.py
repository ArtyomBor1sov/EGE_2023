for num in range(2000000, 3000001):
    counter = 0
    for div in range(int(num ** 0.5), 1349, -1):
        if num % div == 0:
            if num // div - div <= 115:
                counter += 1
            else:
                break
    if counter >= 3:
        print(num)
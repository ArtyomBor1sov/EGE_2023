for num in range(245690, 245757):
    counter = 0
    for div in range(2, num):
        if num % div == 0:
            counter += 1
            break
    if counter == 0:
        print(num - 245689, num)
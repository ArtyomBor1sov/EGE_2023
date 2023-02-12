num = 452022
counter = 0
while counter < 5:
    M = 0
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            M = div + num // div
            break
    if M % 7 == 3:
        print(num, M)
        counter += 1
    num += 1
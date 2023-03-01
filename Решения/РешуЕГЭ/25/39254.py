num = 500000001
counter = 0
while counter < 5:
    divs = []
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            divs.append(div)
            if div != num // div:
                divs.append(num // div)
    if len(divs) >= 6:
        divs.sort()
        M = 1
        for i in range(1, 6):
            M *= divs[i]
        if M < num:
            print(M)
            counter += 1
    num += 1
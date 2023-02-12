num = 10000001
counter = 0
while counter < 5:
    divs = []
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            divs.append(div)
            if div != num // div:
                divs.append(num // div)
    if len(divs) >= 3:
        divs.sort()
        M = divs[-3] + divs[-2]
        if M < 10000:
            print(M)
            counter += 1
    num += 1
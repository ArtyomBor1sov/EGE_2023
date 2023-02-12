num = 600001
counter = 0
while counter < 5:
    divs = []
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            if div % 10 == 7 and div != 7:
                divs.append(div)
            if div != num // div and (num // div) % 10 == 7:
                divs.append(num // div)
    if len(divs) > 0:
        divs.sort()
        print(num, divs[0])
        counter += 1
    num += 1
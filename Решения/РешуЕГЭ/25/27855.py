for num in range(95632, 95700):
    divs = []
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            if div % 2 == 0:
                divs.append(div)
            if div != num // div and (num // div) % 2 == 0:
                divs.append(num // div)
            if len(divs) > 6:
                break
    if len(divs) == 6:
        divs.sort()
        print(divs)
for num in range(185311, 185331):
    divs = []
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            divs.append(div)
            if div != num // div:
                divs.append(num // div)
            if len(divs) > 4:
                break
    if len(divs) == 4:
        divs.sort()
        print(divs)
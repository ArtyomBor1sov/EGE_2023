for num in range(95632, 95651):
    divs = []
    for div in range(1, num + 1):
        if num % div == 0 and div % 2 != 0:
            divs.append(div)
            if len(divs) > 6:
                break
    if len(divs) == 6:
        print(divs[0], divs[1], divs[2], divs[3], divs[4], divs[5])
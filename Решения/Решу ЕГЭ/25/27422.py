for num in range(174457, 174506):
    divs = []
    for div in range(2, num):
        if num % div == 0:
            divs.append(div)
            if len(divs) > 2:
                break
    if len(divs) == 2:
        print(divs[0], divs[1])
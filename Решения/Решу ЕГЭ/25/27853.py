for num in range(312614, 312652):
    divs = []
    for div in range(1, num + 1):
        if num % div == 0:
            divs.append(div)
            if len(divs) > 6:
                break
    if len(divs) == 6:
        print(divs[0], divs[1], divs[2], divs[3], divs[4], divs[5])
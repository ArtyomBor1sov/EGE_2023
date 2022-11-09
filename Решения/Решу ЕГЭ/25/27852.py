for num in range(185311, 185331):
    divs = []
    for div in range(1, num + 1):
        if num % div == 0:
            divs.append(div)
            if len(divs) > 4:
                break
    if len(divs) == 4:
        print(divs[0], divs[1], divs[2], divs[3])
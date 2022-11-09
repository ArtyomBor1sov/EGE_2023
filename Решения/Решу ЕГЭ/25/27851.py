for num in range(210235, 210301):
    divs = []
    for div in range(2, num):
        if num % div == 0:
            divs.append(div)
            if len(divs) > 4:
                break
    if len(divs) == 4:
        print(divs[0], divs[1], divs[2], divs[3])
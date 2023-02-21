for x in range(37):
    num = (1 + 4) * 37 ** 3 + (2 + x) * 37 ** 2 + (3 + 5) * 37 + (x + 9)
    if num % 36 == 0:
        print(num // 36)
        break
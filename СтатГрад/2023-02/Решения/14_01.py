p = 10
while True:
    for x in range(1, p):
        for y in range(1, p):
            if (3 * p ** 3 + 2 * p ** 2 + x * p + 8) + (x * p ** 3 + x * p ** 2 + x * p + 9) == (y * p ** 3 + y * p ** 2 + 2):
                print(x, y, p)
    p += 1
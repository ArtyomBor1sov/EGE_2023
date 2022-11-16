A = 81
while True:
    is_OK = True
    for x in range(1, 91):
        if not (((72 % x == 0) <= (90 % x != 0)) or (A - x > 80)):
            is_OK = False
            break
    if is_OK:
        print(A)
        break
    A += 1
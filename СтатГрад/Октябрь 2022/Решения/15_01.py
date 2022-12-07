A = 101
while True:
    is_OK = True
    for x in range(1, 121):
        if not (((72 % x == 0) <= (120 % x != 0)) or (A - x > 100)):
            is_OK = False
            break
    if is_OK:
        print(A)
        break
    A += 1
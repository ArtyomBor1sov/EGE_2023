print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = int((x == (not y)) <= ((z <= (not w)) and (w <= y)))
                print(x, y, z, w, F)
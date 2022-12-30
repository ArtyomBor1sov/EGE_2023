print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = int((w <= (y == z)) and (y == (z <= x)))
                if (x + y + z + w) <= 1 and F == 1:
                    print(x, y, z, w, F, '- первая строчка')
                if 2 <= (x + y + z + w) <= 3 and F == 1:
                    print(x, y, z, w, F, '- вторая строчка')
                if (x + y + z + w) == 1 and F == 0:
                    print(x, y, z, w, F, '- третья строчка')
                

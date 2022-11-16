minimum = 10 ** 12
for k1 in range(71):
    for k2 in range(71):
        for k3 in range(71):
            for k4 in range(71):
                if 2 * k1 + k3 == 2 * k2 + k4 and k2 + 2 * k4 == 40 and k1 + 2 * k3 > 50:
                    minimum = min(k1 + 2 * k3, minimum)
print(minimum)
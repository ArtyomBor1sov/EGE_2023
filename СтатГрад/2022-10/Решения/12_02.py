maximum = 0
for k1 in range(95):
    for k2 in range(95):
        for k3 in range(95):
            for k4 in range(95):
                if 2 * k1 + k3 == 2 * k2 + k4 and k2 + 2 * k4 == 47 and k1 + 2 * k3 < 70:
                    maximum = max(k1 + 2 * k3, maximum)
print(maximum)
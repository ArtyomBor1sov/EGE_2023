maximum = 0
for num in range(568023, 569231):
    counter = 0
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            counter += 1
            if div != num // div:
                counter += 1
    if counter > maximum:
        maximum = counter
        answer = num
print(maximum, answer)
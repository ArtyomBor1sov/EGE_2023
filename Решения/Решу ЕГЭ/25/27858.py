maximum = 0
for num in range(120115, 120201):
    counter = 0
    for div in range(1, num + 1):
        if num % div == 0:
            counter += 1
    if counter >= maximum:
        maximum = counter
        answer = num
print(maximum, answer)
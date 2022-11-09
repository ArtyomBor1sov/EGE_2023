counter = 0
for num in range(2422000, 2422081):
    div_counter = 0
    for div in range(2, num):
        if num % div == 0:
            div_counter += 1
            break
    if div_counter == 0:
        counter += 1
        print(counter, num)
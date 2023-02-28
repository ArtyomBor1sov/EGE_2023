def summa(x):
    answer = 0
    for symbol in str(x):
        answer += int(symbol)
    return answer

for N in range(15432098, 248756791):
    num = N
    for i in range(3):
        if summa(num) % 2 == 0:
            num = num * 2
        else:
            num = num * 2 + 1
    if 123456789 <= num <= 1987654321:
        first_num = N
        break

for N in range(248756790, 15432097, -1):
    num = N
    for i in range(3):
        if summa(num) % 2 == 0:
            num = num * 2
        else:
            num = num * 2 + 1
    if 123456789 <= num <= 1987654321:
        last_num = N
        break
print(last_num - first_num + 1)
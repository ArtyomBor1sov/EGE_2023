for i in range(10):
    for j in range(10):
        num = int('12345' + str(i) + '7' + str(j) + '8')
        if num % 23 == 0:
            print(num, num // 23)
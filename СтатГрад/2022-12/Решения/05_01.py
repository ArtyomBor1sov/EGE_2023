N = 2 ** 7
while True:
    bin_N = bin(N)[2:]
    for i in range(3):
        summa = 0
        for symbol in str(int(bin_N, 2)):
            summa += int(symbol)
        if summa % 2 == 0:
            bin_N += '0'
        else:
            bin_N += '1'
    if int(bin_N, 2) > 1028:
        print(int(bin_N, 2))
        break
    N += 1
N = 1
while True:
    bin_N = bin(N)[2:]
    new_bin_N = ''
    for i in range(len(bin_N)):
        if bin_N[i] == '0':
            new_bin_N += '1'
        else:
            new_bin_N += '0'
    new_N = int(new_bin_N, 2)
    if N - new_N == 979:
        print(N)
        break
    N += 1
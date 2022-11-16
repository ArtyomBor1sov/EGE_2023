values = '0123456789ABCDEF'
for i in range(16):
    num_1 = int('2' + values[i] + 'BAD', 16)
    num_2 = int('3C' + values[i] + 'FE', 16)
    if (num_1 + num_2) % 15 == 0:
        print((num_1 + num_2) // 15)
        break
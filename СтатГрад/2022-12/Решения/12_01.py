minimum = 10 ** 12
for num in range(2 ** 20):
    stroka = bin(num)[2:]
    stroka = '0' * (20 - len(stroka)) + stroka
    if stroka.count('0') == 10:
        stroka = stroka.replace('1', '2')
        stroka = stroka.replace('0', '1')
        stroka = '0' + stroka + '0'
        while '00' not in stroka:
            stroka = stroka.replace('012', '30', 1)
            if '011' in stroka:
                stroka = stroka.replace('011', '20', 1)
                stroka = stroka.replace('022', '40', 1)
            else:
                stroka = stroka.replace('01', '10', 1)
                stroka = stroka.replace('02', '101', 1)
        if stroka.count('1') == 7 and stroka.count('2') == 5 and stroka.count('3') < minimum:
            minimum = stroka.count('3')
print(minimum)
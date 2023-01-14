from itertools import *

minimum = 10 ** 12
for element in product('12', repeat = 20):
    if element.count('1') == 10:
        stroka = ''
        for symbol in element:
            stroka += symbol
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
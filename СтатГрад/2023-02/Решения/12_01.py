k3 = 9
minimum = 10 ** 12
for k1 in range(7):
    for k2 in range(34):
        for k4 in range(7):
            if (k1 + k2 - k4 == k3 + 3 * k4) and (k1 + k4) == 6 and k2 + k4 == 3:
                minimum = k2 + k4
print(minimum)

# ПРОВЕРКА
#
# from itertools import *
#
# for element in product('12', repeat = 18):
#     if element.count('1') == 9:
#         s = ''
#         for symbol in element:
#             s += symbol
#         s = '0' + s + '0'
#         while '00' not in s:
#             if '011' in s:
#                 s = s.replace('011', '101', 1)
#             else:
#                 s = s.replace('01', '40', 1)
#                 s = s.replace('02', '20', 1)
#                 s = s.replace('0222', '1401', 1)
#         if s.count('4') == 3:
#             print(s)
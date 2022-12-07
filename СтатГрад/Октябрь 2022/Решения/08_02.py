def perevod(num, osn):
    values = '012345678'
    result = ''
    while num > 0:
        result = values[num % osn] + result
        num = num // osn
    return result

counter = 0
for num in range(9 ** 5, 9 ** 6):
    s = perevod(num, 9)
    if s.count('4') == 1 and (s.count('1') + s.count('3') + s.count('5') + s.count('7')) == 2:
        counter += 1
print(counter)

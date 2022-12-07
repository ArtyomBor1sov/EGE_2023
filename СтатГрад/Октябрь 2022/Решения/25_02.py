answers = []
for i in range(10):
    i = str(i)
    num = int('1' + i + '95421')
    if num % 3023 == 0:
        answers.append(num)
    for j in range(10):
        j = str(j)
        num = int('1' + i + '954' + j + '21')
        if num % 3023 == 0:
            answers.append(num)
    for j in range(100):
        j = str(j)
        j = '0' * (2 - len(j)) + j
        num = int('1' + i + '954' + j + '21')
        if num % 3023 == 0:
            answers.append(num)
    for j in range(1000):
        j = str(j)
        j = '0' * (3 - len(j)) + j
        num = int('1' + i + '954' + j + '21')
        if num % 3023 == 0:
            answers.append(num)
answers.sort()
for answer in answers:
    print(answer)

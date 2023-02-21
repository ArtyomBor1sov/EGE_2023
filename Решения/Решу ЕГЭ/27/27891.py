f = open('files/27891_A.txt')
N = int(f.readline())
max_14 = 0
max_7 = 0
max_2 = 0
max_1 = [0, 0]
for line in f:
    num = int(line)
    if num % 14 == 0 and num > max_14:
        max_14 = num
    elif num % 7 == 0 and num > max_7:
        max_7 = num
    elif num % 2 == 0 and num > max_2:
        max_2 = num
    if num > max_1[0]:
        max_1[1] = max_1[0]
        max_1[0] = num
    elif num > max_1[1]:
        max_1[1] = num
if max_14 != max_1[0]:
    print(max(max_14 * max_1[0], max_7, max_2))
else:
    print(max(max_14 * max_1[1], max_7, max_2))

f = open('files/27891_B.txt')
N = int(f.readline())
max_14 = 0
max_7 = 0
max_2 = 0
max_1 = [0, 0]
for line in f:
    num = int(line)
    if num % 14 == 0 and num > max_14:
        max_14 = num
    elif num % 7 == 0 and num > max_7:
        max_7 = num
    elif num % 2 == 0 and num > max_2:
        max_2 = num
    if num > max_1[0]:
        max_1[1] = max_1[0]
        max_1[0] = num
    elif num > max_1[1]:
        max_1[1] = num
if max_14 != max_1[0]:
    print(max(max_14 * max_1[0], max_7, max_2))
else:
    print(max(max_14 * max_1[1], max_7, max_2))
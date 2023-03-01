f = open('files/5879_A.txt')
N = int(f.readline())
nums = []
for line in f:
    nums.append(int(line))
nums = nums * 2
data = {}
summa = 0
counter = 0
maximum = 0
for i in range(2 * N):
    summa += nums[i]
    counter += 1
    if summa % 13 == 0 and counter % 13 == 0 and counter <= N:
        maximum = max(summa, maximum)
    elif (summa % 13, counter % 13) in data:
        for left_summa, left_counter in data[(summa % 13, counter % 13)]:
            if counter - left_counter <= N:
                maximum = max(summa - left_summa, maximum)
                break
    if (summa % 13, counter % 13) not in data:
        data[(summa % 13, counter % 13)] = []
    data[(summa % 13, counter % 13)].append((summa, counter))
print(maximum)

f = open('files/5879_B.txt')
N = int(f.readline())
nums = []
for line in f:
    nums.append(int(line))
nums = nums * 2
data = {}
summa = 0
counter = 0
maximum = 0
for i in range(2 * N):
    summa += nums[i]
    counter += 1
    if summa % 13 == 0 and counter % 13 == 0 and counter <= N:
        maximum = max(summa, maximum)
    elif (summa % 13, counter % 13) in data:
        for left_summa, left_counter in data[(summa % 13, counter % 13)]:
            if counter - left_counter <= N:
                maximum = max(summa - left_summa, maximum)
                break
    if (summa % 13, counter % 13) not in data:
        data[(summa % 13, counter % 13)] = []
    data[(summa % 13, counter % 13)].append((summa, counter))
print(maximum)
f = open('files/33199_A.txt')
N = int(f.readline())
summa_1 = 0
summa_2 = 0
summa_3 = 0
min_diff = 10 ** 12
for line in f:
    nums = [int(x) for x in line.split()]
    nums.sort()
    summa_1 += nums[0]
    summa_2 += nums[1]
    summa_3 += nums[2]
    if (nums[2] - nums[1]) % 2 != 0 and nums[2] - nums[1] < min_diff:
        min_diff = nums[2] - nums[1]
    elif (nums[2] - nums[0]) % 2 != 0 and nums[2] - nums[0] < min_diff:
        min_diff = nums[2] - nums[0]
if summa_1 % 2 == summa_2 % 2:
    summa_3 -= min_diff
print(summa_3)

f = open('files/33199_B.txt')
N = int(f.readline())
summa_1 = 0
summa_2 = 0
summa_3 = 0
min_diff = 10 ** 12
for line in f:
    nums = [int(x) for x in line.split()]
    nums.sort()
    summa_1 += nums[0]
    summa_2 += nums[1]
    summa_3 += nums[2]
    if (nums[2] - nums[1]) % 2 != 0 and nums[2] - nums[1] < min_diff:
        min_diff = nums[2] - nums[1]
    elif (nums[2] - nums[0]) % 2 != 0 and nums[2] - nums[0] < min_diff:
        min_diff = nums[2] - nums[0]
if summa_1 % 2 == summa_2 % 2:
    summa_3 -= min_diff
print(summa_3)
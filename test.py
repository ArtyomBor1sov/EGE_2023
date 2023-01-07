'''
ПАРЫ ПОДРЯД ИДУЩИХ ЭЛЕМЕНТОВ

for i in range(len(nums) - 1):
    print(nums[i], nums[i + 1])

ТРОЙКИ ПОДРЯД ИДУЩИХ ЭЛЕМЕНТОВ

for i in range(len(nums) - 2):
    print(nums[i], nums[i + 1], nums[i + 2])

ПАРЫ РАЗЛИЧНЫХ ЭЛЕМЕНТОВ

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
    print(nums[i], nums[j])

ТРОЙКИ РАЗЛИЧНЫХ ЭЛЕМЕНТОВ

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
    print(nums[i], nums[j], nums[k])
'''

f = open('37373.txt', 'r')
nums = []
for line in f:
    nums.append(int(line))
counter = 0
maximum = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if abs(nums[i] - nums[j]) % 36 == 0 and (nums[i] % 13 == 0 or nums[j] % 13 == 0):
            counter += 1
            maximum = max(abs(nums[i] - nums[j]), maximum)
print(counter, maximum)
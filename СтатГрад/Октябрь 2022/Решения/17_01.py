f = open('../files/17.txt', 'r')
minimum = 10 ** 12
nums = []
for line in f:
    num = int(line)
    if abs(num) % 10 == 7 and num < minimum:
        minimum = num
    nums.append(num)
counter = 0
maximum = 0
for i in range(len(nums) - 1):
    if ((abs(nums[i]) % 10 == 7 and abs(nums[i + 1]) % 10 != 7) or (abs(nums[i]) % 10 != 7 and abs(nums[i + 1]) % 10 == 7)) and (nums[i] ** 2 + nums[i + 1] ** 2 < minimum ** 2):
        counter += 1
        maximum = max(nums[i] ** 2 + nums[i + 1] ** 2, maximum)
print(counter, maximum)
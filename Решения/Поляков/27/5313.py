f = open('files/5313_A.txt')
N, D = [int(x) for x in f.readline().split()]
nums = [int(line) for line in f]
data = {}
for i in range(D):
    data[i] = {}
counter = 0
summa = 0
for i in range(len(nums)):
    counter += data[summa % D].get(nums[i], 0)
    summa += nums[i]
    data[summa % D][nums[i]] = data[summa % D].get(nums[i], 0) + 1
    if i > 0 and nums[i - 1] == nums[i]:
        counter -= 1
print(counter)

f = open('files/5313_B.txt')
N, D = [int(x) for x in f.readline().split()]
nums = [int(line) for line in f]
data = {}
for i in range(D):
    data[i] = {}
counter = 0
summa = 0
for i in range(len(nums)):
    counter += data[summa % D].get(nums[i], 0)
    summa += nums[i]
    data[summa % D][nums[i]] = data[summa % D].get(nums[i], 0) + 1
    if i > 0 and nums[i - 1] == nums[i]:
        counter -= 1
print(counter)
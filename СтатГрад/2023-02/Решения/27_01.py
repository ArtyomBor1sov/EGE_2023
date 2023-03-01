f = open('../files/27-A.txt')
N = int(f.readline())
data = {}
nums = []
counter = 0
for i in range(N):
    num = int(f.readline())
    ost = num % 8
    deg = 0
    while num % 3 == 0 and deg < 7:
        num = num // 3
        deg += 1
    nums.append((ost, deg))
    if i >= 18:
        data[nums[i - 18]] = data.get(nums[i - 18], 0) + 1
    for j in range(7 - deg, 8):
        counter += data.get(((8 - ost) % 8, j), 0)
print(counter)

f = open('../files/27-B.txt')
N = int(f.readline())
data = {}
nums = []
counter = 0
for i in range(N):
    num = int(f.readline())
    ost = num % 8
    deg = 0
    while num % 3 == 0 and deg < 7:
        num = num // 3
        deg += 1
    nums.append((ost, deg))
    if i >= 18:
        data[nums[i - 18]] = data.get(nums[i - 18], 0) + 1
    for j in range(7 - deg, 8):
        counter += data.get(((8 - ost) % 8, j), 0)
print(counter)
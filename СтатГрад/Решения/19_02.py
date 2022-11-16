def make_nums(num):
    nums = []
    if (num + 1) % 3 != 0:
        nums.append(num + 1)
    if (num + 2) % 3 != 0:
        nums.append(num + 2)
    if (num * 2) % 3 != 0:
        nums.append(num * 2)
    return nums

def is_OK(num, turn):
    nums = make_nums(num)
    if turn == 1:
        for i in nums:
            if i >= 151 or not is_OK(i, turn + 1):
                return False
        return True
    else:
        for i in nums:
            if i >= 151:
                return True
        return False

for S in range(1, 150):
    if S % 3 != 0 and is_OK(S, 1):
        print(S)
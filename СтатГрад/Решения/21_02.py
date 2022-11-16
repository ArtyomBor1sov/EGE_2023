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
        next_results = []
        for i in nums:
            if i >= 151 or not is_OK(i,turn + 1):
                return False
            for j in make_nums(i):
                if j >= 151:
                    next_results.append(True)
                    break
            else:
                next_results.append(False)
        if not any(next_results) or all(next_results):
            return False
        return True
    elif turn == 2:
        for i in nums:
            if i >= 151 or is_OK(i, turn + 1):
                return True
        return False
    elif turn == 3:
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
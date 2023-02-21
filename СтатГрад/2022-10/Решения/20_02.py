from functools import lru_cache

def moves(num):
    nums = []
    if (num + 1) % 3 != 0:
        nums.append(num + 1)
    if (num + 2) % 3 != 0:
        nums.append(num + 2)
    if (num * 2) % 3 != 0:
        nums.append(num * 2)
    return nums

@lru_cache(None)
def game(num):
    if num >= 151:
        return 'W'
    if any(game(i) == 'W' for i in moves(num)):
        return 'W1'
    if all(game(i) == 'W1' for i in moves(num)):
        return 'L1'
    if any(game(i) == 'L1' for i in moves(num)):
        return 'W2'
    if all(game(i) == 'W1' or game(i) == 'W2' for i in moves(num)):
        return 'L2'

for S in range(1, 150):
    if S % 3 != 0 and game(S) == 'W2':
        print(S)
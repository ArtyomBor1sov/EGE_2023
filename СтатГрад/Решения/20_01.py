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
    if num >= 103:
        return 'W'
    if any(game(i) == 'W' for i in moves(num)):
        return 'П1'
    if all(game(i) == 'П1' for i in moves(num)):
        return 'В1'
    if any(game(i) == 'В1' for i in moves(num)):
        return 'П2'
    if all(game(i) == 'П1' or game(i) == 'П2' for i in moves(num)):
        return 'В2'

for S in range(1, 102):
    if S % 3 != 0 and game(S) == 'П2':
        print(S)
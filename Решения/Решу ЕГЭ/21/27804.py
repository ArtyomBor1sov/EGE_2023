from functools import lru_cache

def moves(num):
    return [num + 1, num + 4, num * 5]

@lru_cache(None)
def game(num):
    if num >= 68:
        return 'W'
    if any(game(i) == 'W' for i in moves(num)):
        return 'W1'
    if all(game(i) == 'W1' for i in moves(num)):
        return 'L1'
    if any(game(i) == 'L1' for i in moves(num)):
        return 'W2'
    if all(game(i) == 'W1' or game(i) == 'W2' for i in moves(num)):
        return 'L2'

for S in range(1, 68):
    if game(S) == 'L2':
        print(S)
        break
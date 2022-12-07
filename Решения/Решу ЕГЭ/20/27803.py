from functools import lru_cache

def moves(num):
    return [num + 1, num + 4, num * 5]

@lru_cache(None)
def game(num):
    if num >= 68:
        return 'W'
    if any(game(i) == 'W' for i in moves(num)):
        return 'П1'
    if all(game(i) == 'П1' for i in moves(num)):
        return 'В1'
    if any(game(i) == 'В1' for i in moves(num)):
        return 'П2'

for S in range(1, 68):
    if game(S) == 'П2':
        print(S)
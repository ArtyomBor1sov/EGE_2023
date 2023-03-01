from functools import *

def moves(num_1, num_2):
    data = []
    for i in range(1, min(num_1, num_2) + 1):
        data.append([min(num_1, num_2) + i, max(num_1, num_2)])
    return data

@lru_cache(None)
def game(num_1, num_2):
    if num_1 + num_2 > 45:
        return 'W'
    if any(game(i, j) == 'W' for i, j in moves(num_1, num_2)):
        return 'W1'
    if all(game(i, j) == 'W1' for i, j in moves(num_1, num_2)):
        return 'L1'
    if any(game(i, j) == 'L1' for i, j in moves(num_1, num_2)):
        return 'W2'

for S in range(1, 41):
    if game(5, S) == 'W2':
        print(S)
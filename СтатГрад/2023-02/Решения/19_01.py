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

minimum = 10 ** 12
for x in range(1, 45):
    for y in range(1, 45):
        if game(x, y) == 'W1':
            minimum = min(x + y, minimum)
print(minimum)
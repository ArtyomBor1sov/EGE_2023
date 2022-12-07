from functools import lru_cache
from math import ceil

def moves(nums):
    a, b = nums
    moves = []
    if a > 0:
        moves.append((a - 1, b))
    if b > 0:
        moves.append((a, b - 1))
    if a > 1:
        moves.append((ceil(a / 2), b))
    if b > 1:
        moves.append((a, ceil(b / 2)))
    return moves

@lru_cache(None)
def game(nums):
    if sum(nums) <= 20:
        return 'W'
    if any(game(i) == 'W' for i in moves(nums)):
        return 'W1'
    if all(game(i) == 'W1' for i in moves(nums)):
        return 'L1'
    if any(game(i) == 'L1' for i in moves(nums)):
        return 'W2'
    if all(game(i) == 'W1' or game(i) == 'W2' for i in moves(nums)):
        return 'L2'

for S in range(11, 160):
    if game((10, S)) == 'L2':
        print(S)
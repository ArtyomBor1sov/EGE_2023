f = open('files/5244_B.txt')
N = int(f.readline())
primes = [True] * 100001
primes[0], primes[1] = False, False
for i in range(2, 100001):
    if primes[i]:
        for j in range(2 * i, 100001, i):
            primes[j] = False
dividers = {}
max_counter = 0
min_len = 10 ** 12
for i in range(N):
    num = int(f.readline())
    for div in range(1, int(num ** 0.5) + 1):
        if num % div == 0:
            if primes[div]:
                dividers[div] = i
            if div != num // div and primes[num // div]:
                dividers[num // div] = i
    if len(dividers) > max_counter:
        max_counter = len(dividers)
        min_length = i - min(dividers.values()) + 1
    elif len(dividers) == max_counter:
        min_length = min(i - min(dividers.values()) + 1, min_length)
print(min_length)
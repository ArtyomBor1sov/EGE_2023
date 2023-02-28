f = open('files/5290_A.txt')
N = int(f.readline())
primes = [True] * 10001
primes[0], primes[1] = False, False
data = {}
for i in range(2, 10001):
    if primes[i]:
        data[i] = [-1]
        for j in range(i * 2, 10001, i):
            primes[j] = False
maximum = 0
for i in range(N):
    num = int(f.readline())
    curr_maximum = 0
    for key, val in data.items():
        if num % key == 0:
            curr_maximum = max(i - val[-1], curr_maximum)
        else:
            val.append(i)
    maximum = max(curr_maximum, maximum)
print(maximum)

f = open('files/5290_B.txt')
N = int(f.readline())
primes = [True] * 10001
primes[0], primes[1] = False, False
data = {}
for i in range(2, 10001):
    if primes[i]:
        data[i] = [-1]
        for j in range(i * 2, 10001, i):
            primes[j] = False
maximum = 0
for i in range(N):
    num = int(f.readline())
    curr_maximum = 0
    for key, val in data.items():
        if num % key == 0:
            curr_maximum = max(i - val[-1], curr_maximum)
        else:
            val.append(i)
    maximum = max(curr_maximum, maximum)
print(maximum)
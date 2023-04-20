f = open('files/5315-A.txt')
N, K = [int(x) for x in f.readline().split()]
data = [int(line) for line in f]
sum_left = 0
sum_right = 0
counter_0 = 0
answer = 0
for i in range(K):
    if i < K // 2:
        sum_left += data[i]
    elif i > K // 2:
        sum_right += data[i]
    if data[i] == 0:
        counter_0 += 1
if sum_left == sum_right and counter_0 > 0:
    answer += 1
for i in range(1, N - K + 1):
    sum_left += data[i + K // 2 - 1] - data[i - 1]
    sum_right += data[i + K - 1] - data[i + K // 2]
    if data[i - 1] == 0:
        counter_0 -= 1
    if data[i + K - 1] == 0:
        counter_0 += 1
    if sum_left == sum_right and counter_0 > 0:
        answer += 1
print(answer)

f = open('files/5315-B.txt')
N, K = [int(x) for x in f.readline().split()]
data = [int(line) for line in f]
sum_left = 0
sum_right = 0
counter_0 = 0
answer = 0
for i in range(K):
    if i < K // 2:
        sum_left += data[i]
    elif i > K // 2:
        sum_right += data[i]
    if data[i] == 0:
        counter_0 += 1
if sum_left == sum_right and counter_0 > 0:
    answer += 1
for i in range(1, N - K + 1):
    sum_left += data[i + K // 2 - 1] - data[i - 1]
    sum_right += data[i + K - 1] - data[i + K // 2]
    if data[i - 1] == 0:
        counter_0 -= 1
    if data[i + K - 1] == 0:
        counter_0 += 1
    if sum_left == sum_right and counter_0 > 0:
        answer += 1
print(answer)
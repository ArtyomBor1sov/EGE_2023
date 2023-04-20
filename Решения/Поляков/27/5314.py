f = open('files/5314-A.txt')
N, K, D = [int(x) for x in f.readline().split()]
data = {}
counter_0 = 0
answer = 0
for line in f:
    if int(line) == 0:
        counter_0 += 1
    else:
        ost_D = int(line) % D
        ost_K = counter_0 % K
        if ((D - ost_D) % D, ost_K) in data:
            answer += data[((D - ost_D) % D, ost_K)]
        data[(ost_D, ost_K)] = data.get((ost_D, ost_K), 0) + 1
print(answer)

f = open('files/5314-B.txt')
N, K, D = [int(x) for x in f.readline().split()]
data = {}
counter_0 = 0
answer = 0
for line in f:
    if int(line) == 0:
        counter_0 += 1
    else:
        ost_D = int(line) % D
        ost_K = counter_0 % K
        if ((D - ost_D) % D, ost_K) in data:
            answer += data[((D - ost_D) % D, ost_K)]
        data[(ost_D, ost_K)] = data.get((ost_D, ost_K), 0) + 1
print(answer)
f = open('files/40742.txt')
N = int(f.readline())
week_start = 1633305600
week_end = week_start + 604800
counter = 0
data = [0] * 604800
for line in f:
    start, end = [int(x) for x in line.split()]
    if (start < week_start or start == 0) and (end >= week_start or end == 0):
        counter += 1
    if week_start <= start < week_end:
        data[start - week_start] += 1
    if week_start <= end < week_end:
        data[end - week_start] -= 1
maximum = counter
max_time = 0
for element in data:
    counter += element
    if counter > maximum:
        maximum = counter
        max_time = 1
    elif counter == maximum:
        max_time += 1
print(maximum, max_time)
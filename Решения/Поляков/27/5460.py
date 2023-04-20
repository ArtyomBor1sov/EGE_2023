f = open('files/5460_A.txt')
N = int(f.readline())
data = [int(line) for line in f] * 2
full_sum = sum(data) // 2
closest_sum = 0
min_length = N
left_ind = 0
right_ind = -1
curr_sum = 0
while left_ind < N:
    right_ind += 1
    curr_sum += data[right_ind]
    while curr_sum > full_sum // 2:
        curr_sum -= data[left_ind]
        left_ind += 1
    if curr_sum > closest_sum:
        closest_sum = curr_sum
        min_length = min(right_ind - left_ind, N - (right_ind - left_ind) - 2)
    elif curr_sum == closest_sum:
        min_length = min([right_ind - left_ind, N - (right_ind - left_ind) - 2, min_length])
print(min_length)

f = open('files/5460_B.txt')
N = int(f.readline())
data = [int(line) for line in f] * 2
full_sum = sum(data) // 2
closest_sum = 0
min_length = N
left_ind = 0
right_ind = -1
curr_sum = 0
while left_ind < N:
    right_ind += 1
    curr_sum += data[right_ind]
    while curr_sum > full_sum // 2:
        curr_sum -= data[left_ind]
        left_ind += 1
    if curr_sum > closest_sum:
        closest_sum = curr_sum
        min_length = min(right_ind - left_ind, N - (right_ind - left_ind) - 2)
    elif curr_sum == closest_sum:
        min_length = min([right_ind - left_ind, N - (right_ind - left_ind) - 2, min_length])
print(min_length)
f = open('../files/26.txt', 'r')
N = int(f.readline())
nums = []
for line in f:
    nums.append(int(line))
nums.sort()
answer = []
for i in range(N):
    for j in range(len(answer)):
        if nums[i] - answer[j][-1] >= 7:
            answer[j].append(nums[i])
            break
    else:
        answer.append([nums[i]])
print(len(answer))
maximum = 0
for element in answer:
    maximum = max(len(element), maximum)
print(maximum)
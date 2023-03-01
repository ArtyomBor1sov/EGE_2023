f = open('files/33769.txt')
line = f.readline()
counter = {}
for i in range(2, len(line)):
    if line[i - 1] == line[i - 2]:
        counter[line[i]] = counter.get(line[i], 0) + 1
maximum = 0
for key, val in counter.items():
    if val > maximum:
        maximum = val
        max_letter = key
print (max_letter)

# f = open('files/33769.txt', 'r')
# line = f.readline()
# counter = [0] * 26
# for i in range(2, len(line)):
#     if line[i - 1] == line[i - 2]:
#         counter[ord(line[i]) - ord('A')] += 1
# max_ind = 0
# for i in range(len(counter)):
#     if counter[i] > counter[max_ind]:
#         max_ind = i
# print(chr(ord('A') + max_ind))

# f = open('files/33769.txt', 'r')
# line = f.readline()
# letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# counter = [0] * 26
# for i in range(2, len(line)):
#     if line[i - 1] == line[i - 2]:
#         counter[letters.find(line[i])] += 1
# max_ind = 0
# for i in range(len(counter)):
#     if counter[i] > counter[max_ind]:
#         max_ind = i
# print(letters[max_ind])
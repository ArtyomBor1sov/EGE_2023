f = open('files/35482.txt')
minimum = 10 ** 12
for line in f:
    if line.count('G') < minimum:
        minimum = line.count('G')
        min_line = line
maximum = 0
for code in range(ord('A'), ord('Z') + 1):
    if min_line.count(chr(code)) >= maximum:
        maximum = min_line.count(chr(code))
        max_letter = chr(code)
print(max_letter)
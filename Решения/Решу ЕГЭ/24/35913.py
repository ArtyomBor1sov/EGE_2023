f = open('files/35913.txt')
minimum = 10 ** 12
for line in f:
    if line.count('N') < minimum:
        minimum = line.count('N')
        min_line = line
maximum = 0
for code in range(ord('A'), ord('Z') + 1):
    if min_line.count(chr(code)) >= maximum:
        maximum = min_line.count(chr(code))
        max_letter = chr(code)
print(max_letter)
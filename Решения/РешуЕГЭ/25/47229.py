from fnmatch import *

for num in range(0, 10 ** 10 + 1, 2023):
    if fnmatch(str(num), '1?2139*4'):
        print(num, num // 2023)

# for num in range(0, 10 ** 10 + 1, 2023):
#     s = str(num)
#     if s[0] == '1' and s[2:6] == '2139' and s[-1] == '4':
#         print(num, num // 2023)
from fnmatch import *

for num in range(0, 10 ** 10, 2023):
    if fnmatch(str(num), '1?493*41'):
        print(num)

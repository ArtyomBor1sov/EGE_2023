from fnmatch import *

for num in range(0, 10 ** 10, 4173):
    if fnmatch(str(num), '1?7246*1'):
        print(num)
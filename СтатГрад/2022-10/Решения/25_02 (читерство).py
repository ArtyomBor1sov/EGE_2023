from fnmatch import *

for num in range(0, 10 ** 10, 3023):
    if fnmatch(str(num), '1?954*21'):
        print(num)
